import os

from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")
discord_guild_id = os.getenv("DISCORD_GUILD_ID")
github_url = os.getenv("GITHUB_URL")

def validate_settings():
    if discord_token is None:
        raise ValueError(
            "Falta DISCORD_TOKEN en el archivo .env"
        )
    if discord_guild_id is None:
        raise ValueError(
            "Falta DISCORD_GUILD_ID en el archivo .env"
        )
    if github_url is None:
        raise ValueError(
            "Falta GITHUB_URL en el archivo .env"
        )