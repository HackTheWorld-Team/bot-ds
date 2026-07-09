import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

from database import(
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
load_dotenv()

init_database()

#Actualizaciones del bot
bot_version = get_system_record("bot_version")

print(f"Versión guardada en la base de datos: {bot_version}")
logging.info(f"Versión de ATLAS cargada: {bot_version}")


#Os.getenv para conexion
discord_token = os.getenv("DISCORD_TOKEN")
discord_guild_id = os.getenv("DISCORD_GUILD_ID")
github_url = os.getenv("GITHUB_URL")


guild = discord.Object(id=int(discord_guild_id))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.tree.command(
    name="github",
    description="Muestra el repositorio oficial de ATLAS"
)
@discord.app_commands.guilds(guild)
async def github(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"💻 Repositorio oficial de ATLAS:\n{github_url}"
    )


@bot.tree.command(
    name="ping",
    description="Comprueba si ATLAS está funcionando"
)
@discord.app_commands.guilds(guild)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🟢 ATLAS está funcionando correctamente."
    )

@bot.tree.command(
        name="ayuda",
        description="Muestra los comandos disponibles de ATLAS"
)
@discord.app_commands.guilds(guild)
async def ayuda(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🤖 **ATLAS - Comandos disponibles**\n\n"
        "🟢 `/ping` - Comprueba si ATLAS está funcionando\n"
        "💻 `/github` - Muestra el repositorio oficial de la comunidad\n"
        "❓ `/ayuda` - Muestra esta lista de comandos"
    )


@bot.event
async def on_ready():
    await bot.tree.sync(guild=guild)
    print("Comandos slash sincronizados correctamente.")
    print(f"Bot conectado como {bot.user}")
logging.info("Comandos slash sincronizados correctamente.")
logging.info(f"Bot conectado como {bot.user}")


if discord_token is None:
    print(
        "Error: No se encontró el token de Discord."
    )
else:
    bot.run(discord_token)