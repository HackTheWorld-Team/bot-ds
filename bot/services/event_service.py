from datetime import datetime

from sqlalchemy import select

from bot.database.database import SessionLocal
from bot.models.events import Event


def save_event(
    discord_event_id: int,
    name: str,
    description: str | None,
    start_time: datetime,
    end_time: datetime,
    organizer_id: int,
) -> None:
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
                organizer_id=organizer_id,
            )

            db.add(event)
            db.commit()