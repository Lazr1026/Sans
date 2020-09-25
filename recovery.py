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

client.remove_command('help')

@commands.has_any_role('Owner')
@client.command()
async def recover(ctx):
    await ctx.send("Performing recovery. Please make sure the latest git commit is in a working state.")
    subprocess.run(['sudo', '/home/pi/duckdns/sans.sh'])
@commands.has_any_role('Owner')
@client.command()
async def showerr(ctx):
    await ctx.send("Please wait while the error status is obtained. This will take around 10 seconds.")
    err = subprocess.run(['bash', '/home/pi/duckdns/err.sh'], stdout=subprocess.PIPE)
    err = err.stdout
    err = str(err)
    err = err.replace('\\n', '\n')
    err = "Error (or command output): \n" + "```" + err + "```"
    await ctx.send(err)

client.run(token)
