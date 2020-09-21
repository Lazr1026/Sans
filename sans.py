import discord
import asyncio 
from discord.ext import commands 
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('I Am Ready')

@client.command()
async def guide(ctx):
    await ctx.send('Options are: 3ds, wiiu, nx')

@client.command()
async def guide_3ds(ctx):
    await ctx.send('https://youtu.be/8yh6h_iwl6I')

@client.command()
async def guide_wiiu(ctx):
    await ctx.send('https://wiiu.hacks.guide')

@client.command()
async def guide_nx(ctx):
    await ctx.send('https://nh-server.github.io/switch-guide/')

@client.command()
async def cartinstall(ctx):
    await ctx.send('https://youtu.be/pzbfHQ6uTcU')

@client.command() 
async def dump_nds(ctx):
    await ctx.send('https://youtu.be/x-Et2zkl3Ek')

@client.command()
async def dump_3ds(ctx):
    await ctx.send('https://youtu.be/b1Ng-b0fnpg')

@client.command()
async def pirate(ctx):
    await ctx.send('We do not support nor condone piracy as it is\n 1. Against Discord TOS\n 2. It is illegal, buy your damn games')

@client.command()
async def lumacheck(ctx):
    await ctx.send('How to check your luma version\n\n 1. Power off your console\n 2. Press and hold the SELECT button, then press power while still holding SELECT\n 3. Send a picture of the luma configuration')

@client.command()
async def sdlock(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757705136612180118/image0.png')

@client.command()
async def sdroot(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757705163220713632/image0.png')

@client.command()
async def invite(ctx):
    await ctx.send('Invilid Syntax, Options Are: ivan, homebrew')

@client.command()
async def invite_ivan(ctx):
    await ctx.send('https://discord.com/invite/eRP5pjA')

@client.command()
async def invite_homebrew(ctx):
    await ctx.send('discord.gg/nintendohomebrew')

@client.command()
async def r4(ctx):
    await ctx.send('An R4 is a Flashcart that can or cannot be used for ntrboot (unbrick and cfw installation tool I guess you can call it). Its also used to play gaems (hopefully dumped from carts).')

@client.command()
async def cfwuses(ctx):
    await ctx.send('Options are 3ds, wiiu, nx')

@client.command()
async def cfwuses_3ds(ctx):
    await ctx.send('https://3ds.eiphax.tech/tips.html')

@client.command()
async def cfwuses_nx(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757743046086623272/dssd.PNG')

@client.command()
async def cfwuses_wiiu(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757744237440794654/wiiu_cfw.PNG')

@client.command()
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮‍♂️')
async def ban(ctx, member : discord.Member, *,reason=0):
    await member.ban(reason=reason)

client.run('')
