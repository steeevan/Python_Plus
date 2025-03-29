import discord
from discord.ext import commands

class ReactionRole(commands.Cog):
    """Assign roles based on user reactions."""

    def __init__(self, bot):
        self.bot = bot
        self.role_message_id = None  # Store message ID for tracking reactions
        self.emoji_to_role = {
            "🎮": "Gamer",
            "🎨": "Artist",
            "💻": "Coder",
        }

    @commands.command(name="setup_roles")
    @commands.has_permissions(administrator=True)
    async def setup_roles(self, ctx):
        """Sends a message that assigns roles when users react to it."""
        embed = discord.Embed(title="🎭 Role Selection",
                              description="React to get a role:\n"
                                          "🎮 → Gamer\n"
                                          "🎨 → Artist\n"
                                          "💻 → Coder",
                              color=discord.Color.blue())
        message = await ctx.send(embed=embed)

        for emoji in self.emoji_to_role.keys():
            await message.add_reaction(emoji)

        self.role_message_id = message.id  # Store message ID

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Assigns roles when users react to the role selection message."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        role_name = self.emoji_to_role.get(payload.emoji.name)
        if role_name:
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                await member.add_roles(role)
                print(f"✅ Assigned {role.name} to {member.name}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Removes roles when users remove their reaction."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        role_name = self.emoji_to_role.get(payload.emoji.name)
        if role_name:
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                await member.remove_roles(role)
                print(f"❌ Removed {role.name} from {member.name}")

async def setup(bot):
    await bot.add_cog(ReactionRole(bot))
