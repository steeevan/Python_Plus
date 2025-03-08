from discord.ext import commands
import random

class Fun(commands.Cog):
    '''Fun Commands for the bot'''

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        '''Replies with Pong! and the bots latency.'''
        latency = round(self.bot.latency * 1000,2)
        await ctx.send(f"Pong! Latency: {latency}ms")

    @commands.command(name="numberguess")
    async def number_guess(self, ctx):
        """Guess a number between 1 and 10."""
        number = random.randint(1, 10)
        await ctx.send("I'm thinking of a number between 1 and 10. Try to guess!")

        def check(m):
            return m.author == ctx.author and m.content.isdigit()
        
        try:
            guess = await self.bot.wait_for("message", timeout=10.0, check=check)
            if guess.content == number:
                await ctx.send(f"Correct! The number was {number}")
            else:
                await ctx.send(f"Incorrect! The number was {number}")
        except:
            await ctx.send("TImes up")
    

async def setup(bot):
    await bot.add_cog(Fun(bot))