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
            existing_event = Event(
                discord_event_id=discord_event_id,
                name=name,
                description=description,
                start_time=start_time,
                end_time=end_time,
                organizer_id=organizer_id,
            )

            db.add(existing_event)
        else:
            existing_event.name = name
            existing_event.description = description
            existing_event.start_time = start_time
            existing_event.end_time = end_time
            existing_event.organizer_id = organizer_id

        db.commit()
def update_event_status(
    discord_event_id: int,
    status: str,
) -> bool:
    with SessionLocal() as db:
        event = db.scalar(
            select(Event).where(
                Event.discord_event_id == discord_event_id
            )
        )

        if event is None:
            return False

        event.status = status
        db.commit()

        return True


def list_events() -> list[dict]:
    with SessionLocal() as db:
        events = db.scalars(
            select(Event).order_by(Event.start_time.desc())
        ).all()

        return [
            {
                "name": event.name,
                "description": event.description,
                "start_time": event.start_time.isoformat(),
                "end_time": event.end_time.isoformat(),
                "organizer_id": event.organizer_id,
                "status": event.status,
            }
            for event in events
        ]