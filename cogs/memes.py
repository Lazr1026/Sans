import discord
from discord.ext import commands 

class memes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def halp(self, ctx):
        '''You want some help?'''
        await ctx.send("No.")

    @commands.command()
    async def pat(self, ctx):
        '''Pats.'''
        await ctx.send("https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819")
    
    @commands.command()
    async def basil(self, ctx):
        '''Facts.'''
        await ctx.send("Basil is <:meowawau:754767499253383300>")

    @commands.command()
    async def snas(self, ctx):
        '''Fortnire Battle Pass'''
        await ctx.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

    @commands.command()
    async def nh(self, ctx):
        '''nh bad'''
        await ctx.send('Nintendo Homebrew mods have shown a marked lack of care about bans on elsewhere lately. However,such things as pyrosee in asschans and memes in off topic are known causes for Discord account bans in the past.\nYou should enable invisible mode while talking in Nintendo Homebrew and not talking to pbanj as these seem to be high risk at this time.')

    @commands.command()
    async def k(self, ctx):
        '''k'''
        await ctx.send('https://tenor.com/view/kermit-sesame-street-write-gif-4298020')

def setup(client):
    client.add_cog(memes(client))
