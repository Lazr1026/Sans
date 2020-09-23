print('init')
import discord
import subprocess
print('stage0')
import asyncio 
print('stage1')
from discord.ext import commands
print('stage2')
client = commands.Bot(command_prefix = '.')
print('botStage')

tokenfile = open("/home/pi/Sans/recoverytoken", "r")
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print('Ready.')

@commands.has_any_role('Owner')
@client.command()
async def recover(ctx):
    await ctx.send("Performing recovery. Please make sure the latest git commit is in a working state.")
    subprocess.run(['sudo', '/home/pi/duckdns/sans.sh'])

client.run(token)
