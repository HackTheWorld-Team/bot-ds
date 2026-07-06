import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

#variables guardadas
load_dotenv()
discord_token = os.getenv("discord_token")
discord_guild_id = os.getenv("discord_guild_id")

guild = discord.Object(id=int(discord_guild_id))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.tree.command(
    name="ping", description="Responde con 'Pong!'"
)
@discord.app_commands.guilds(guild)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


@bot.event
async def on_ready():
    await bot.tree.sync(guild=guild)
    print("Comandos slash sincronizados correctamente.")
    print(f"Bot conectado como {bot.user}")

if discord_token is None:
    print("Error: No se encontró el token de Discord. Asegúrate de tener un archivo .env con la variable 'discord_token'.")
else:
    bot.run(discord_token)