import discord 
from discord.ext import commands

class bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def sans (self, ctx):
        '''Sans Github Repo'''
        embed = make_embed(
        title="Sans",
        author="Maintained by Lazr",
        color=discord.Color.green(),
        thumbnail="https://i.imgur.com/AkOLH6q.png",
        url="https://github.com/Lazr1026/Sans",
        description="Sans, The discord bot that is kinda useful!"
    )
        await ctx.send(embed=embed)

    @commands.command()
    async def contributors(self, ctx):
        '''Links to the Github contributors page'''
        embed = make_embed(
            title="Contributors",
            url="https://github.com/Lazr1026/Sans/graphs/contributors",
            description="Sans Contributors",
    )
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(seld, ctx):
        await ctx.send(f':ping_pong:! Latency is {int(bot.latency * 1000)} ms!')

def setup(client):
    client.add_cog(bot(client))
