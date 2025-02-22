import discord
from discord.ext import commands
import config
import logging
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BotClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True  # Enable message event handling
        intents.message_content = True  # IMPORTANT: Needed for text commands
        intents.guilds = True
        super().__init__(command_prefix=config.COMMAND_PREFIX, intents=intents)

    async def on_ready(self):
        logging.info(f"Bot connected as {self.user}")

    async def load_cog(self):
        """Loads only the fun.py cog for testing"""
        await self.load_extension("cogs.fun")
        logging.info("Loaded cog: fun")

bot = BotClient()

if __name__ == "__main__":
    async def main():
        await bot.load_cog()  # Load only fun.py
        await bot.start(config.BOT_TOKEN)

    asyncio.run(main())
