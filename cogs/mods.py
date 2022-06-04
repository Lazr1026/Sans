import discord
import os
import subprocess
from discord.ext import commands

class mods(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def ban(self, ctx, member: discord.User = None, reason=""):
        '''Ban Users. Admin+'''
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself.")
            return
        reasonraw = ctx.message.content[28:]
        message = f"You have been banned from {ctx.guild.name} for the reason {reasonraw}"
        await ctx.guild.ban(member, reason=reasonraw, delete_message_days=0)
        await ctx.channel.send(f"{member} has been b&. 👍")
        await member.send(message)

    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def kick(self, ctx, member: discord.Member, *, reason=0):
        '''Kick users. Admin+'''
        await member.kick(reason=reason, delete_message_days=0)
        send = f"user {member.name} has been kicked."
        await ctx.send(send)

    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def say(self, ctx, message):
        '''The bot is sentient.'''
        await ctx.message.delete()
        await ctx.send(ctx.message.content[5:])

    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def update(self, ctx):
        await ctx.send("Updating code. The bot will be down for roughly 15 seconds.")
        subprocess.run(['bash', home_path + '/sans.sh'])

def setup(client):
    client.add_cog(mods(client))
