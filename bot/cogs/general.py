import logging

import discord
from discord import app_commands
from discord.ext import commands

from bot.config import settings

logger = logging.getLogger(__name__)

GUILD = discord.Object(id=int(settings.discord_guild_id))

COMANDO_EMOJIS: dict[str, str] = {
    "ping": "🟢",
    "github": "💻",
    "ayuda": "❓",
}


class GeneralCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Comprueba si ATLAS está funcionando",
    )
    @app_commands.guilds(GUILD)
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            "🟢 ATLAS está funcionando correctamente."
        )

    @app_commands.command(
        name="github",
        description="Muestra el repositorio oficial de ATLAS",
    )
    @app_commands.guilds(GUILD)
    async def github(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"💻 Repositorio oficial de ATLAS:\n{settings.github_url}"
        )

    @app_commands.command(
        name="ayuda",
        description="Muestra los comandos disponibles de ATLAS",
    )
    @app_commands.guilds(GUILD)
    async def ayuda(self, interaction: discord.Interaction) -> None:
        comandos = sorted(
            self.bot.tree.get_commands(guild=GUILD),
            key=lambda comando: comando.name,
        )
        lineas = "\n".join(
            f"{COMANDO_EMOJIS.get(comando.name, '•')} "
            f"`/{comando.name}` - {comando.description}"
            for comando in comandos
        )
        mensaje = "🤖 **ATLAS - Comandos disponibles**\n\n" + lineas
        await interaction.response.send_message(mensaje)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GeneralCog(bot))
    logger.info("GeneralCog cargado correctamente.")