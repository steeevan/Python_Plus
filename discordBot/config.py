import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

#bot configuration
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
COMMAND_PREFIX = "$"