print('Loading...')
import discord
import subprocess
from os import system
import asyncio 
from discord.ext import commands
bot = commands.Bot(command_prefix = '.')

tokendir = os.path.dirname(os.path.realpath(__file__))
with open(tokendir + "/recoverytoken") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')

bot.remove_command('help')

@commands.has_any_role('Owner')
@bot.command()
async def recover(ctx):
    await ctx.send("Performing recovery. Please make sure the latest git commit is in a working state.")
    subprocess.run(['sudo', '/home/pi/duckdns/sans.sh'])

@commands.has_any_role('Owner')
@bot.command()
async def showerr(ctx):
    await ctx.send("Please wait while the error status is obtained. This will take around 10 seconds.")
    cmd = "bash /home/pi/duckdns/err.sh"
    system(cmd)
    errfile = open("/home/pi/ram/err", "r")
    err = errfile.read()
    errfile.close()
    cmd = "bash /home/pi/duckdns/del.sh"
    system(cmd)
    err = "Error (or command output): \n" + "```" + err + "```"
    await ctx.send(err)

@bot.command()
async def code(ctx):
    await ctx.send("https://github.com/Lazr1026/Sans")

bot.run(token)
