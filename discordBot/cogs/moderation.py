import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    """Moderation commands for managing users."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Kicks a user from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} has been kicked! Reason: {reason}")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Bans a user from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member.mention} has been banned! Reason: {reason}")

    async def ensure_muted_role(self, guild):
        """Creates a Muted role if it doesn't exist and sets correct permissions."""
        role = discord.utils.get(guild.roles, name="Muted")
        if not role:
            role = await guild.create_role(name="Muted", reason="Needed for muting users")

            for channel in guild.text_channels:
                await channel.set_permissions(role, send_messages=False)

            for channel in guild.voice_channels:
                await channel.set_permissions(role, speak=False)

            print(f"✅ Created 'Muted' role in {guild.name}")

        return role
    
    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, time: int = 10):
        """Mutes a user for a specified time (in minutes)."""
        role = await self.ensure_muted_role(ctx.guild)

        if role in member.roles:
            return await ctx.send(f"❌ {member.mention} is already muted.")

        await member.add_roles(role)
        await ctx.send(f"🔇 {member.mention} has been muted for {time} minutes.")

        await asyncio.sleep(time * 60)
        await member.remove_roles(role)
        await ctx.send(f"🔊 {member.mention} has been unmuted!")

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Deletes a number of messages."""
        await ctx.channel.purge(limit=amount + 1)  # +1 to delete command message itself
        await ctx.send(f"🗑️ Cleared {amount} messages.", delete_after=3)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
