import discord
from discord.ext import commands
import openai
import config
import asyncio

class ChatGPT(commands.Cog):
    """A Cog to interact with OpenAI's ChatGPT API with rate limiting."""

    def __init__(self, bot):
        self.bot = bot
        openai.api_key = config.OPENAI_API_KEY
        self.cooldowns = {}  # Track cooldowns per user

    @commands.command(name="ask")
    async def ask(self, ctx, *, question: str):
        """Asks ChatGPT a question and returns an AI-generated response."""
        
        user_id = ctx.author.id

        # Check cooldown (Users can only send a request every 10 seconds)
        if user_id in self.cooldowns and self.cooldowns[user_id] > asyncio.get_event_loop().time():
            remaining_time = int(self.cooldowns[user_id] - asyncio.get_event_loop().time())
            await ctx.send(f"⏳ Please wait {remaining_time} seconds before asking again.")
            return
        
        await ctx.send("🤖 Thinking...")  

        try:
            client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use GPT-3.5 instead of GPT-4
                messages=[{"role": "user", "content": question}],
                max_tokens=150,
                temperature=0.7
            )

            answer = response.choices[0].message.content
            await ctx.send(f"🧠 ChatGPT says: {answer}")

            # Set cooldown (10 seconds per request per user)
            self.cooldowns[user_id] = asyncio.get_event_loop().time() + 10  

        except openai.APIError as e:
            await ctx.send("❌ OpenAI is currently overloaded. Try again later.")
            print(f"APIError: {e}")

        except openai.RateLimitError:
            await ctx.send("❌ You are sending too many requests! Try again later.")
        
        except openai.AuthenticationError:
            await ctx.send("❌ Invalid API key. Check your config file.")

        except openai.OpenAIError as e:
            await ctx.send("❌ An unexpected error occurred.")
            print(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(ChatGPT(bot))
