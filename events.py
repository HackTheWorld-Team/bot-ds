from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, select
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    discord_event_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    end_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    organizer_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="scheduled"
    )

    reminder_48_sent: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    reminder_24_sent: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )


def save_event(
    discord_event_id: int,
    name: str,
    description: str | None,
    start_time: datetime,
    end_time: datetime,
    organizer_id: int
) -> None:
    from database import SessionLocal

    with SessionLocal() as db:
        existing_event = db.scalar(
            select(Event).where(
                Event.discord_event_id == discord_event_id
            )
        )

        if existing_event is None:
            event = Event(
                discord_event_id=discord_event_id,
                name=name,
                description=description,
                start_time=start_time,
                end_time=end_time,
                organizer_id=organizer_id
            )

            db.add(event)
            db.commit()