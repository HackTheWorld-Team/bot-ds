from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
)


class Base(DeclarativeBase):
    pass


class SystemRecord(Base):
    __tablename__ = "system_records"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    value: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )


DATABASE_URL = "sqlite:///atlas.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine
)


def init_database() -> None:
    # Se importa aquí para evitar una importación circular.
    from events import Event  # noqa: F401

    Base.metadata.create_all(bind=engine)


def set_system_record(key: str, value: str) -> None:
    with SessionLocal() as db:
        record = db.scalar(
            select(SystemRecord).where(
                SystemRecord.key == key
            )
        )

        if record is None:
            record = SystemRecord(
                key=key,
                value=value
            )
            db.add(record)
        else:
            record.value = value

        db.commit()


def get_system_record(key: str) -> str | None:
    with SessionLocal() as db:
        record = db.scalar(
            select(SystemRecord).where(
                SystemRecord.key == key
            )
        )

        if record is None:
            return None

        return record.value