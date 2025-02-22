from discord.ext import commands

class Fun(commands.Cog):
    '''Fun Commands for the bot'''

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        '''Replies with Pong! and the bots latency.'''
        latency = round(self.bot.latency * 1000,2)
        await ctx.send(f"Pong! Latency: {latency}ms")


async def setup(bot):
    await bot.add_cog(Fun(bot))