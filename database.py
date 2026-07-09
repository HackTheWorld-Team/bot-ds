from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker
)

DATABASE_URL = "sqlite:///atlas.db"
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

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    bind= engine
)

def init_database():
    Base.metadata.create_all(bind=engine)