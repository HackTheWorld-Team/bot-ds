import os

from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")
discord_guild_id = os.getenv("DISCORD_GUILD_ID")
github_url = os.getenv("GITHUB_URL")