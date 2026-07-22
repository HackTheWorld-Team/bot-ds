import discord
from discord.ext import commands
from bot.services.event_service import (
    save_event,
    update_event_status,
)

class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_scheduled_event_create(
        self,
        event: discord.ScheduledEvent,
    ) -> None:
        save_event(
            discord_event_id=event.id,
            name=event.name,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time or event.start_time,
            organizer_id=event.creator_id or 0,
        )
        print(f"Nuevo evento guardado: {event.name}")

    @commands.Cog.listener()
    async def on_scheduled_event_update(
        self,
        before: discord.ScheduledEvent,
        after: discord.ScheduledEvent,
    ) -> None:
        save_event(
            discord_event_id=after.id,
            name=after.name,
            description=after.description,
            start_time=after.start_time,
            end_time=after.end_time or after.start_time,
            organizer_id=after.creator_id or 0,
        )
        print(f"Evento actualizado: {after.name}")

    @commands.Cog.listener()
    async def on_scheduled_event_delete(
        self,
        event: discord.ScheduledEvent,
    ) -> None:
        updated = update_event_status(
            discord_event_id=event.id,
            status="cancelled",
        )

        if updated:
            print(f"Evento cancelado: {event.name}")
        else:
            print(
                f"No se encontró el evento eliminado en la base de datos: "
                f"{event.name}"
            )