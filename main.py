import logging

import discord
from discord.ext import commands

from bot.config import settings
settings.validate_settings()
print(
    "Token cargado desde settings:",
    bool(settings.discord_token)
)

from bot.database.database import(
    get_system_record,
    init_database,
    set_system_record,
)

logging.basicConfig(
    filename="logs/atlas.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Variables guardada
init_database()


# Actualizaciones del bot
set_system_record("bot_version", "0.1.0")
bot_version = get_system_record("bot_version")

print(f"Versión guardada en la base de datos: {bot_version}")
logging.info(f"Versión de ATLAS cargada: {bot_version}")



guild = discord.Object(
    id=int(settings.discord_guild_id)
)

intents = discord.Intents.default()
intents.message_content = True
intents.guild_scheduled_events = True 

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def setup_hook() -> None:
    await bot.load_extension("bot.cogs.general")
    await bot.load_extension("bot.cogs.events")

    await bot.tree.sync(guild=guild)

    print("Comandos slash sincronizados correctamente.")
    logging.info("Comandos slash sincronizados correctamente.")


@bot.event
async def on_ready() -> None:
    print(f"Bot conectado como {bot.user}")
    logging.info(f"Bot conectado como {bot.user}")


if settings.discord_token is None:
    print("Error: No se encontró el token de Discord."
    )
else:
    bot.run(settings.discord_token)