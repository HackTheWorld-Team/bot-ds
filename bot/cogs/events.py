import discord
from discord.ext import commands
from bot.services.event_service import save_event

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