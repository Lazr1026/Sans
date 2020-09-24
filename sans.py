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

tokenfile = open("/home/pi/Sans/token", "r")
token = tokenfile.read()
tokenfile.close()

client.remove_command('help')

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
    if ctx.message.content == ".guide wii":
        await ctx.send('https://wii.guide')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, wiiu, wii, nx')

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
    if ctx.message.content == ".dump wiiu":
        await ctx.send('https://wiiu.hacks.guide/#/dump-games')
        sent = 1
    if ctx.message.content == ".dump vwii":
        await ctx.send('https://wiiu.hacks.guide/#/dump-wii-games')
        sent = 1
    if ctx.message.content == ".dump wii":
        await ctx.send('https://wii.guide/dump-games')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, ds, wiiu, vwii, wii')

@client.command()
async def invite(ctx):
    sent = 0
    if ctx.message.content == ".invite ivan":
        await ctx.send('https://discord.com/invite/eRP5pjA')
        sent = 1
    if ctx.message.content == ".invite homebrew":
        await ctx.send('discord.gg/C29hYvh')
        sent = 1
    if ctx.message.content == ".invite analog":
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
        await ctx.send('https://media.discordapp.net/attachments/439933093118476289/692162539261526047/image0.png?width=343&height=395')
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
    await ctx.send('Link to SANS source code \nhttps://github.com/Lazr1026/Sans')

@client.command()
async def radeon(ctx):
    await ctx.send('radeon says she\'s gonna hardmod another 3ds, prepare to lose some brain cells.')
@client.command()
async def uwuham(ctx):
    await ctx.send('yes we know. js is better than py')
@client.command()
async def credits(ctx):
    await ctx.send('Lazr: creator and programmer \nRadeon: programmer \nUwUham: telling us discord.js is better')
@client.command()
async def sdformat(ctx):
    await ctx.send('Common sd formatting tools:\n\n Windows-<http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm>\n\n Linux-<https://gparted.org/download.php> + <https://github.com/dosfstools/dosfstools>\n\n MacOS-<https://support.apple.com/guide/disk-utility/format-a-disk-for-windows-computers-dskutl1010>\n\n MacOS: Always select "MS-DOS (FAT)", even if the card is larger than 32GB.')
@client.command()
async def lazr(ctx):
    await ctx.send('lazr says they want to hardmod, prepare to gain some brain cells')
    
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
        sample = getLstmSample(checkpointName)
        await ctx.send(sample)
        sent = 1
    if sent == 0:
        await ctx.send('Invalid LSTM directive.')

def getLstmCheckpoint():
    checkpoints = subprocess.run(['bash', '/home/pi/checkpoints.sh'], stdout=subprocess.PIPE)
    checkpoints = checkpoints.stdout
    checkpoints = str(checkpoints)
    checkpoints = checkpoints.replace('\\n', '\n')
    checkpoints = "Checkpoints: \n" + "```" + checkpoints + "```"
    return checkpoints

def getLstmSample(checkpointName):
    sample = subprocess.run(['bash', '/home/pi/sample.sh', checkpointName], stdout=subprocess.PIPE)
    sample = sample.stdout
    sample = str(sample)
    sample = sample.replace('\\n', '\n')
    sample = "Sample: \n" + "```" + sample + "```"
    return sample

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
@client.command()
@commands.has_any_role('Owner')
async def update(ctx):
    await ctx.send("Updating code. The bot will be down for roughly 2 minutes.")
    subprocess.run(['sudo', '/home/pi/duckdns/sans.sh'])

@client.command()
async def local58(ctx):
    await ctx.send('`THERE ARE NO FACES`')
    await ctx.send('`DO NOT LOOK AT THE MOON`')

@client.command()
async def snas(ctx):
    await ctx.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

@client.command()
async def help(ctx):
    sent = 0
    if ctx.message.content == ".help assistance":
        await ctx.send('```Assistance commands are: cartinstall, cfwusues, dump, guide, lumabug, lumacheck, nospace, notbricked, r4, sdlock, sdroot```')
        sent = 1
    if ctx.message.content == ".help cartinstall":
        await ctx.send('```Shows the guide for cartinstall```')
        sent = 1
    if ctx.message.content == ".help cfwuses":
        await ctx.send('```Shows what you can do with cfw```')
        sent = 1
    if ctx.message.content == ".help dump":
        await ctx.send('```Shows the guide for how to dump your games```')
        sent = 1
    if ctx.message.content == ".help guide":
        await ctx.send('```.Shows the guide to install CFW on your console```')
        sent = 1
    if ctx.message.content == ".help lumabug":
        await ctx.send('```.lumabug\n\n Shows how to solve the lumabug```')
        sent = 1
    if ctx.message.content == ".help lumacheck":
        await ctx.send('```.Shows how to check your luma version```')
        sent = 1
    if ctx.message.content == ".help nospace":
        await ctx.send('```Shows how to make a nand backup without enough space on your sd card```')
        sent = 1
    if ctx.message.content == ".help notbricked":
        await ctx.send('```Shows that you are not bricked```')
        sent = 1
    if ctx.message.content == ".help r4":
        await ctx.send('```Says what an r4 is and what it does/its uses```')
        sent = 1
    if ctx.message.content == ".help sdlock":
        await ctx.send('```.Shows how to unlock your sd card```')
        sent = 1
    if ctx.message.content == ".help sdroot":
        await ctx.send('```Shows what the root of an sd card is```')
        sent = 1
    if ctx.message.content == ".help invite":
        await ctx.send('```Invite commands are: ivan, homebrew, a secret one```')
        sent = 1
    if ctx.message.content == ".help ivan":
        await ctx.send('```An invite to internet ivans discord server```')
        sent = 1
    if ctx.message.content == ".help homebrew":
        await ctx.send('```An invite to Nintendo Homebrews discord server```')
        sent = 1
    if ctx.message.content == ".help memes":
        await ctx.send('```Memes are: radeon, snas, uwuham, lazr```')
        sent = 1
    if ctx.message.content == ".help radeon":
        await ctx.send('```Type the command```')
        sent = 1
    if ctx.message.content == ".help snas":
        await ctx.send('```Type the command```')
        sent = 1
    if ctx.message.content == ".help uwuham":
        await ctx.send('```Type the command```')
        sent = 1
     if ctx.message.content == ".help lazr":
        await ctx.send('```Type the command```')
        sent = 1
     if sent == 0:
        await ctx.send('What can I help you with?\n\n assistnce\n invite\n memes')
client.run(token)

