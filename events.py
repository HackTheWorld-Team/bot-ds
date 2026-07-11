from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

#Creamos las clases de eventos
class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    discord_event_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=True
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    star_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    end_time: Mapped[DateTime] = mapped_column(
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