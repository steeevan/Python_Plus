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
        intents.messages = True
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        intents.reactions = True
        
        super().__init__(command_prefix=config.COMMAND_PREFIX, intents=intents)
        self.initial_cogs = [
            "cogs.fun",
            "cogs.moderation",
            "cogs.reaction_roles",
            "cogs.chatgpt"  # ✅ Load ChatGPT integration
        ]



    async def on_ready(self):
        logging.info(f"✅ Bot connected as {self.user}")

    async def load_cogs(self):
        """Loads all necessary cogs."""
        for cog in self.initial_cogs:
            try:
                await self.load_extension(cog)
                logging.info(f"✅ Loaded cog: {cog}")
            except Exception as e:
                logging.error(f"❌ Failed to load cog {cog}: {e}")

bot = BotClient()

if __name__ == "__main__":
    async def main():
        await bot.load_cogs()  # Load all cogs
        await bot.start(config.BOT_TOKEN)

    asyncio.run(main())
