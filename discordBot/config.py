import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

#bot configuration
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = "$"