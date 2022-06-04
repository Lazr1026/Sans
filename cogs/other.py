import discord
from discord.ext import commands

class other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pfp"])
    async def profile(self, ctx, user: discord.User):
        '''Fetch a user's profile picture'''
        await ctx.send(f'Profile image for user: {user.name}')
        pfp = user.avatar_url
        await ctx.send(pfp)

    @commands.command()
    async def invite(self, ctx, invite):
        '''Link invites to other servers'''
        invites = {
            "ivan": "NM85JqJ",
            "nh": "C29hYvh"
        }
        try: await ctx.send(f'https://discord.gg/{invites[invite.lower()]}')
        except: await ctx.send('Options are: ivan, nh')

    @commands.command()
    async def socials(self, ctx):
        '''Links to Ivans socials'''
        await ctx.send('Internet Ivans socials: https://flow.page/internetivan')

def setup(client):
    client.add_cog(other(client))
