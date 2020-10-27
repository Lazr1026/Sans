print('Loading...')
import discord
import subprocess
import os
import asyncio 
from discord.ext import commands
bot = commands.Bot(command_prefix = '!')

tokendir = os.path.dirname(os.path.realpath(__file__))
with open(tokendir + "/recoverytoken") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')

bot.remove_command('help')

@commands.has_any_role('Owner', 'Admin')
@bot.command()
async def recover(ctx):
    await ctx.send("Performing recovery. Please make sure the latest git commit is in a working state.")
    subprocess.run(['sudo', '/home/lucas/Documents/recovery/sans.sh'])

@commands.has_any_role('Owner')
@bot.command()
async def showerr(ctx):
    await ctx.send("Please wait while the error status is obtained. This will take around 10 seconds.")
    cmd = "bash /home/pi/duckdns/err.sh"
    os.system(cmd)
    errfile = open("/home/pi/ram/err", "r")
    err = errfile.read()
    errfile.close()
    cmd = "bash /home/pi/duckdns/del.sh"
    os.system(cmd)
    err = "Error (or command output): \n" + "```" + err + "```"
    await ctx.send(err)

@bot.group()
@commands.has_any_role('Owner', 'Admin')
async def ctl(ctx):
    '''for use by admins'''
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid argument.")

@ctl.command()
async def update(ctx):
    await ctx.send("Updating code. The bot will be down for roughly 15 seconds.")
    subprocess.run(['sudo', '/home/lucas/Documents/recovery/sans.sh'])

@ctl.command()
async def reboot(ctx):
    await ctx.send("Rebooting host. Let\'s hope it comes back online.")
    subprocess.run(['sudo', 'reboot'])

@ctl.command()
async def service(ctx):
    await ctx.send("Restarting systemd service.")
    subprocess.run(['sudo', 'systemctl', 'restart', 'sans'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'sansrecovery'])

@bot.command()
async def code(ctx):
    await ctx.send("https://github.com/Lazr1026/Sans")

bot.run(token)
