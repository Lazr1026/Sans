import discord 
from discord.ext import commands

def make_embed(title=None, description=None, author=None, thumbnail=None, url=None, color=None, image=None, name=None) -> discord.Embed: 
    """Cleaner way to make embeds
    Thumbnail and author are taken as kwargs, title is default "Guide" """ 
    if isinstance(color, int):
        color = discord.Color(color)
    
    embed = discord.Embed(
        title=title,
        color=color,
        url=url,
        description=description
    )
    if name is not None:   embed.set_author(name=name)
    if image is not None:   embed.set_image(url=image)
    if thumbnail is not None:   embed.set_thumbnail(url=thumbnail)
    return embed

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
            color=discord.Color.blurple(),
            url="https://github.com/Lazr1026/Sans/graphs/contributors",
            description="Sans Contributors",
    )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(bot(client))
