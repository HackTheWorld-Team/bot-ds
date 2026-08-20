import logging
import os
from logging.handlers import RotatingFileHandler

import discord
from discord.ext import commands

from bot.config import settings

logger = logging.getLogger("atlas")

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "atlas.log")
LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUP_COUNT = 5


def configure_logging() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)

    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
    )

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler],
    )


settings.validate_settings()
configure_logging()

logger.info("Token cargado desde settings: %s", bool(settings.discord_token))

from bot.database.database import (
    get_system_record,
    init_database,
    set_system_record,
)

# Variables guardada
init_database()


# Actualizaciones del bot
set_system_record("bot_version", "0.1.0")
bot_version = get_system_record("bot_version")

logger.info("Versión de ATLAS cargada: %s", bot_version)



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

    logger.info("Comandos slash sincronizados correctamente.")


@bot.event
async def on_ready() -> None:
    logger.info("Bot conectado como %s", bot.user)


def main() -> None:
    if settings.discord_token is None:
        logger.error("Error: No se encontró el token de Discord.")
        return
    bot.run(settings.discord_token)


if __name__ == "__main__":
    main()