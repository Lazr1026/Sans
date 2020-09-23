print('init')
import discord
print('stage0')
import asyncio 
print('stage1')
from discord.ext import commands
print('stage2')
client = commands.Bot(command_prefix = '.')
print('botStage')

tokenfile = open("token", "r")
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print('Ready.')

@client.command()
async def guide(ctx):
    sent = 0
    if ctx.message.content == ".guide 3ds":
        await ctx.send('https://youtu.be/8yh6h_iwl6I')
        sent = 1
    if ctx.message.content == ".guide wiiu":
        await ctx.send('https://wiiu.hacks.guide')
        sent = 1
    if ctx.message.content == ".guide nx":
        await ctx.send('https://nh-server.github.io/switch-guide/')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, wiiu, nx')

@client.command()
async def cartinstall(ctx):
    await ctx.send('https://youtu.be/pzbfHQ6uTcU')
@client.command() 
async def dump(ctx):
    sent = 0
    if ctx.message.content == ".dump ds":
        await ctx.send('https://youtu.be/x-Et2zkl3Ek')
        sent = 1
    if ctx.message.content == ".dump 3ds":
        await ctx.send('https://youtu.be/b1Ng-b0fnpg')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, ds')

@client.command()
async def invite(ctx):
    sent = 0
    if ctx.message.content == ".invite ivan":
        await ctx.send('https://discord.com/invite/eRP5pjA')
        sent = 1
    if ctx.message.content == ".invite homebrew":
        await ctx.send('discord.gg/C29hYvh')
        sent = 1
    if ctx.message.content == ".invite dimma":
        await ctx.send('discord.gg/sZAaZR9')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: ivan, homebrew, and a secret server.')


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
async def r4(ctx):
    await ctx.send('An R4 is a Flashcart that can or cannot be used for ntrboot (unbrick and cfw installation tool I guess you can call it). Its also used to play gaems (hopefully dumped from carts).')

@client.command()
async def cfwuses(ctx):
    sent = 0
    if ctx.message.content == ".cfwuses 3ds":
        await ctx.send('https://3ds.eiphax.tech/tips.html')
        sent = 1
    if ctx.message.content == ".cfwuses wiiu":
        await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757744237440794654/wiiu_cfw.PNG')
        sent = 1
    if ctx.message.content == ".cfwuses nx":
        await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757744237440794654/wiiu_cfw.PNG')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, wiiu, nx')

@client.command()
async def notbricked(ctx):
    await ctx.send('No, you are not bricked if your power LED turns on and off after you installed b9s, you are not bricked and are just missing a file called boot.firm in the root of your SD card to fix the issue\n 1. Check you inserted the SD card in your console\n 2. Place/replace the file, downloading it from <https://github.com/LumaTeam/Luma3DS/releases>')

@client.command()
async def lumabug(ctx):
    await ctx.send('Luma Black Screen Bug If you have Luma3DS and your console is stuck on a black screen after you power it on, follow these steps:\n 1. Power off the console.\n 2. Take out any game cartridge, but leave the SD card in.\n 3. Power on the console.\n 4. Leave the console open and powered on for 10-15 minutes. Do not touch the console during this time.\n If the console boots successfully in that time, the bug is now fixed and is unlikely to happen again. If the console still fails to boot to home menu, come back and ask for more help. Mention that you have already tried the Luma black screen process.')

@client.command()
async def nospace(ctx):
    await ctx.send('How to make a NAND backup without enough space on your sd card:\n 1. Copy the Nintendo 3DS and the DCIM folder (if you have it) to your computer, then delete them from your SD CARD.\n 2. Boot into GodMode9 and perform the backup again. Once it’s done power off your system.\n 3. Copy all the files in the gm9/out folder on your sd card to a place on your pc. Then delete those files from the SD CARD.\n 4. Copy the Nintendo 3DS and DCIM folder (if you had it) back to your sd card and delete it from your computer.')

@client.command()
async def sans(ctx):
    await ctx.send('https://github.com/Lazr1026/Sans')

@client.command()
async def radeon(ctx):
    await ctx.send('radeon says she\'s gonna hardmod another 3ds, prepare to lose some brain cells.')
@client.command()
async def e(ctx):
    await ctx.send(':wink:')
async def credits(ctx):
    await ctx.send('Lazr: creator and programmer \n Radeon: programmer \n Uwuham: telling us discord.js is better')

@client.command()
async def lstm(ctx):
    sent = 0
    cmd = ctx.message.content[6:]
    send = "LSTM: " + cmd
    await ctx.send(send)
    if cmd == "list":
        checkpointList = getLstmCheckpoint()
        await ctx.send(checkpointList)
        sent = 1
    if cmd.startswith('sample'):
        checkpointName = cmd[7:]
        send = "Sampling " + checkpointName + "..."
        await ctx.send(send)
        sample = subprocess.run(['bash', 'sample.sh', checkpointName], stdout=subprocess.PIPE)
        sample = sample.stdout
        sample = str(sample)
        sample = sample.replace('\\n', '\n')
        sample = "Sample: \n" + "```" + sample + "```"
        await ctx.send(sample)
        sent = 1
    if sent == 0:
        await ctsx.send('Invalid LSTM directive.')
def getLstmCheckpoint():
    checkpoints = subprocess.run(['bash', 'checkpoints.sh'], stdout=subprocess.PIPE)
    checkpoints = checkpoints.stdout
    checkpoints = str(checkpoints)
    checkpoints = checkpoints.replace('\\n', '\n')
    checkpoints = "Checkpoints: \n" + "```" + checkpoints + "```"
    return checkpoints

@client.command()
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮‍♂️')
async def ban(ctx, member : discord.Member, *,reason=0):
    await member.ban(reason=reason)
    send = "user " + str(member) + " has been banned."
    await ctx.send(send)
@client.command()
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮', 'peeps', 'Helper', 'OMEGAMOD')
async def say(ctx, message):
    await ctx.message.delete()
    await ctx.send(ctx.message.content[5:])

client.run(token)
