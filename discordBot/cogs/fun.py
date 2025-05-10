import random
import aiohttp
from discord.ext import commands
import discord

class Fun(commands.Cog):
    """Fun commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Replies with Pong! and the bot's latency."""
        latency = round(self.bot.latency * 1000, 2)
        await ctx.send(f"Pong! 🏓 Latency: {latency}ms")

    @commands.command(name="hello")
    async def hello(self, ctx):
        """Sends a friendly greeting."""
        await ctx.send(f"Hello {ctx.author.mention}! 👋 How's your day?")

    @commands.command(name="joke")
    async def joke(self, ctx):
        """Sends a random joke."""
        jokes = [
            "Why don't skeletons fight each other? Because they don't have the guts! 😂",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "Why did the bicycle fall over? Because it was two-tired! 🚴",
        ]
        await ctx.send(random.choice(jokes))

    @commands.command(name="roll")
    async def roll(self, ctx):
        """Rolls a 6-sided dice."""
        dice_result = random.randint(1, 6)
        await ctx.send(f"🎲 You rolled a {dice_result}!")

    @commands.command(name="flip")
    async def flip(self, ctx):
        """Flips a coin (Heads or Tails)."""
        result = random.choice(["Heads", "Tails"])
        await ctx.send(f"🪙 The coin landed on **{result}**!")

    @commands.command(name="8ball")
    async def eight_ball(self, ctx, *, question: str):
        """Magic 8-ball answers questions."""
        responses = [
            "Yes, absolutely! ✅",
            "No way! ❌",
            "Maybe... 🤔",
            "I don't know, try again later. ⏳",
            "Definitely! 🎯",
            "I wouldn’t count on it. 🚫",
        ]
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {random.choice(responses)}")

    @commands.command(name="meme")
    async def meme(self, ctx):
        """Fetches a random meme from an API."""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://meme-api.com/gimme") as response:
                if response.status == 200:
                    data = await response.json()
                    meme_url = data["url"]
                    await ctx.send(meme_url)
                else:
                    await ctx.send("Failed to fetch a meme 😢")
    @commands.command(name="cat")
    async def cat(self, ctx):
        """Fetches a random cat image."""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as response:
                if response.status == 200:
                    data = await response.json()
                    cat_url = data[0]["url"]
                    await ctx.send(cat_url)
                else:
                    await ctx.send("Couldn't fetch a cat picture 😿")

    @commands.command(name="dog")
    async def dog(self, ctx):
        """Fetches a random dog image."""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as response:
                if response.status == 200:
                    data = await response.json()
                    dog_url = data["message"]
                    await ctx.send(dog_url)
                else:
                    await ctx.send("Couldn't fetch a dog picture 🐶")

    @commands.command(name="rps")
    async def rock_paper_scissors(self, ctx, choice: str):
        """Play Rock, Paper, Scissors with the bot."""
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)

        if choice.lower() not in choices:
            await ctx.send("Please choose rock, paper, or scissors!")
            return

        result = None
        if choice == bot_choice:
            result = "It's a tie! 🤝"
        elif (choice == "rock" and bot_choice == "scissors") or \
             (choice == "paper" and bot_choice == "rock") or \
             (choice == "scissors" and bot_choice == "paper"):
            result = "You win! 🎉"
        else:
            result = "I win! 😈"

        await ctx.send(f"You chose {choice}, I chose {bot_choice}. {result}")

    @commands.command(name="numberguess")
    async def number_guess(self, ctx):
        """Guess a number between 1 and 10."""
        number = random.randint(1, 10)
        await ctx.send("I'm thinking of a number between 1 and 10. Try to guess!")

        def check(m):
            return m.author == ctx.author and m.content.isdigit()

        try:
            guess = await self.bot.wait_for("message", timeout=10.0, check=check)
            if int(guess.content) == number:
                await ctx.send(f"🎉 Correct! The number was {number}.")
            else:
                await ctx.send(f"❌ Wrong! The number was {number}.")
        except:
            await ctx.send("⏳ Time's up! Try again.")

    @commands.command(name="fact")
    async def random_fact(self, ctx):
        """Sends a random fun fact."""
        facts = [
            "Did you know? Honey never spoils! 🍯",
            "Bananas are berries, but strawberries aren't! 🍓🍌",
            "Octopuses have three hearts and blue blood. 🐙",
            "A group of flamingos is called a 'flamboyance'. 🦩",
        ]
        await ctx.send(random.choice(facts))

    @commands.command(name="waifu")
    async def waifu(self, ctx):
        """Fetches a random waifu image."""
        url = "https://api.waifu.pics/sfw/waifu"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    waifu_url = data["url"]
                    embed = discord.Embed(title="Here's a waifu for you! 💖", color=discord.Color.pink())
                    embed.set_image(url=waifu_url)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("❌ Could not fetch a waifu. Please try again later.")
async def setup(bot):
    await bot.add_cog(Fun(bot))
