print('init')
import discord
import subprocess
print('stage0')
import asyncio 
print('stage1')
from discord.ext import commands
from discord.ext.commands import MemberConverter
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
async def pat(ctx):
    await ctx.send("https://imgur.com/gallery/WyMHuyL")

@client.command(name="7zip")
async def _7zip(ctx):
    await ctx.send("WinRAR is not a very good archiving utility. \nYou should use 7-Zip instead. \nhttps://www.7-zip.org/")

@client.command()
async def listhelpers(ctx):
    await ctx.send('Helpers:\n\n __3DS__\n Nintenmike.3dsx\n M1807\n UwUham\n radeon\n\n __Wii U__\n Lazr\n\n __Switch__\n jsjhax34')
    
@client.command()
async def liststaff(ctx):
    await ctx.send('Staff:\n Internet Ivan\n Nintenmike.3dsx\n Lazr')
    
@client.command()
async def guide(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".guide 3ds"):
        await ctx.send('https://youtu.be/8yh6h_iwl6I')
        sent = 1
    if str(ctx.message.content).startswith(".guide wiiu"):
        await ctx.send('https://wiiu.hacks.guide')
        sent = 1
    if str(ctx.message.content).startswith(".guide nx"):
        await ctx.send('https://nh-server.github.io/switch-guide/')
        sent = 1
    if str(ctx.message.content).startswith(".guide wii"):
        await ctx.send('https://wii.guide')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, wiiu, wii, nx')

@client.command()
async def browserhax(ctx):
    await ctx.send('https://3ds.hacks.guide/homebrew-launcher-(browserhax-2020)')
        
@client.command()
async def fredtool(ctx):
    await ctx.send('https://3ds.hacks.guide/installing-boot9strap-(fredtool)')
        
@client.command()
async def soundhax(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".soundhax hbl"):
        await ctx.send('https://3ds.hacks.guide/homebrew-launcher-(soundhax)')
        sent = 1
    if str(ctx.message.content).startswith(".soundhax b9s"):
        await ctx.send('https://3ds.hacks.guide/installing-boot9strap-(soundhax)')
        sent = 1
    if sent == 0:
        await ctx.send('What soundhax would you like? hbl, b9s')
        
@client.command()
async def troubleshoot(ctx):
    await ctx.send('How to troubleshoot seedminer based methods: https://3ds.eiphax.tech/issues.html')
        
@client.command()
async def cartinstall(ctx):
    await ctx.send('https://youtu.be/pzbfHQ6uTcU')
@client.command() 
async def dump(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".dump ds"):
        await ctx.send('https://youtu.be/x-Et2zkl3Ek')
        sent = 1
    if str(ctx.message.content).startswith(".dump 3ds"):
        await ctx.send('https://youtu.be/b1Ng-b0fnpg')
        sent = 1
    if str(ctx.message.content).startswith(".dump wiiu"):
        await ctx.send('https://wiiu.hacks.guide/#/dump-games')
        sent = 1
    if str(ctx.message.content).startswith(".dump vwii"):
        await ctx.send('https://wiiu.hacks.guide/#/dump-wii-games')
        sent = 1
    if str(ctx.message.content).startswith(".dump wii"):
        await ctx.send('https://wii.guide/dump-games')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: 3ds, ds, wiiu, vwii, wii')

@client.command()
async def invite(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".invite ivan"):
        await ctx.send('https://discord.gg/NM85JqJ')
        sent = 1
    if str(ctx.message.content).startswith(".invite homebrew"):
        await ctx.send('discord.gg/C29hYvh')
        sent = 1
    if str(ctx.message.content).startswith(".invite analog"):
        await ctx.send('https://discord.gg/7bXpJSh')
        sent = 1
    if str(ctx.message.content).startswith(".invite chill"):
        await ctx.send('discord.gg/7ECUWDp')
        sent = 1
    if sent == 0:
        await ctx.send('Options are: ivan, homebrew, analog, chill.')
        
@client.command()
async def luma(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".luma latest"):
        await ctx.send('https://github.com/LumaTeam/Luma3DS/releases/tag/v10.2')
        sent = 1
    if str(ctx.message.content).startswith(".luma 7.0.5"):
        await ctx.send('https://github.com/LumaTeam/Luma3DS/releases/tag/v7.0.5')
        sent = 1
    if str(ctx.message.content).startswith(".luma 7.1"):
        await ctx.send('https://github.com/Lazr1026/Sans/edit/master/sans.py')
        sent = 1
    if sent == 0:
        await ctx.send('```What luma version would you like?\n\n latest\n 7.0.5\n 7.1```')


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
async def twlmenu(ctx):
    await ctx.send('https://www.youtube.com/watch?v=07ZMSrrZwCQ')
    
@client.command()
async def twlfix(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".twlfix cfw"):
        await ctx.send('```Use this tool to fix the dsiware on your 3ds!``` <https://github.com/MechanicalDragon0687/TWLFix-CFW/releases/>, please note that you must do a system update after the process has finished')
        sent = 1
    if str(ctx.message.content).startswith(".twlfix 3ds"):
        await ctx.send('```Use this tool to fix the dsiware on your 3ds!``` <https://github.com/MechanicalDragon0687/TWLFix-3DS/releases/>, please note that you must do a system update after the process has finished')
        sent = 1
    if str(ctx.message.content).startswith(".twlfix stock"):
        await ctx.send('```Use this tool to fix the dsiware on your 3ds!``` <https://github.com/MechanicalDragon0687/TWLFix/wiki/Instructions>, please note that you must do a system update after the process has finished')
        sent = 1
    if sent == 0:
        await ctx.send('```What twlfix would ya like? cfw, 3ds, stock```')
    
@client.command()
async def ndsforwarders(ctx):
    await ctx.send('https://gbatemp.net/threads/nds-forwarder-cias-for-your-home-menu.426174/')
    
@client.command()
async def ap(ctx):
    await ctx.send('https://glazedbelmont.github.io/appatching/')
    
@client.command()
async def meta(ctx):
    await ctx.send('you seem to be in <#759902836116160532>')
    
@client.command()
async def cfwuses(ctx):
    sent = 0
    if str(ctx.message.content).startswith(".cfwuses 3ds"):
        await ctx.send('https://3ds.eiphax.tech/tips.html')
        sent = 1
    if str(ctx.message.content).startswith(".cfwuses wiiu"):
        await ctx.send('https://cdn.discordapp.com/attachments/754753360132833431/757744237440794654/wiiu_cfw.PNG')
        sent = 1
    if str(ctx.message.content).startswith(".cfwuses nx"):
        await ctx.send('https://cdn.discordapp.com/attachments/744815170626519062/758814416992075816/Screenshot_20200924-151725_Discord.jpg')
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
async def sd(ctx):
    await ctx.send('How to check your sd card for errors:\n <https://3ds.eiphax.tech/sd.html>')
    
@client.command()
async def sans(ctx):
    await ctx.send('Link to SANS source code \nhttps://github.com/Lazr1026/Sans')
@client.command()
async def profile(ctx, user: discord.User):
    await ctx.send("Profile image for user: " + str(user))
    pfp = user.avatar_url
    await ctx.send(pfp)

@client.command()
async def radeon(ctx):
    await ctx.send('radeon says she\'s gonna hardmod another 3ds, prepare to lose some brain cells.')
@client.command()
async def uwuham(ctx):
    await ctx.send('guys somethings wrong with uwuham hes using python')
@client.command()
async def credits(ctx):
    await ctx.send('Lazr: creator and programmer \nRadeon: programmer \nUwUham: telling us discord.js is better')
@client.command()
async def sdformat(ctx):
    await ctx.send('Common sd formatting tools:\n\n Windows-<http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm>\n\n Linux-<https://gparted.org/download.php> + <https://github.com/dosfstools/dosfstools>\n\n MacOS-<https://support.apple.com/guide/disk-utility/format-a-disk-for-windows-computers-dskutl1010>\n\n MacOS: Always select "MS-DOS (FAT)", even if the card is larger than 32GB.')
@client.command()
async def lazr(ctx):
    await ctx.send('lazr says she wants to hardmod, prepare to gain some brain cells')
    
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
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮‍')
async def ban(ctx, member : discord.Member, *,reason=0):
    await member.ban(reason=reason)
    send = "user " + str(member) + " has been banned."
    await ctx.send(send)
@client.command()
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮‍', 'Helper')
async def kick(ctx, member : discord.Member, *,reason=0):
    await member.kick(reason=reason)
    send = "user "+str(member) + " has been kicked."
    await ctx.send(send)
@client.command()
@commands.has_any_role('Owner', 'Owner 🍙', 'Staff', 'Admin👮‍', 'Helper', 'OMEGAMOD')
async def say(ctx, message):
    await ctx.message.delete()
    await ctx.send(ctx.message.content[5:])
@client.command()
@commands.has_any_role('Owner')
async def update(ctx):
    await ctx.send("Updating code. The bot will be down for roughly 15 seconds.")
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
        await ctx.send('```Assistance commands are: cartinstall, cfwusues, dump, guide, lumabug, lumacheck, nospace, notbricked, r4, sdlock, sdroot, luma, sd, ndsforwarders, ap, vc, troubleshoot, twlfix```')
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
        await ctx.send('```Shows the guide to install CFW on your console```')
        sent = 1
    if ctx.message.content == ".help lumabug":
        await ctx.send('```lumabug\n\n Shows how to solve the lumabug```')
        sent = 1
    if ctx.message.content == ".help lumacheck":
        await ctx.send('```Shows how to check your luma version```')
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
        await ctx.send('```Shows how to unlock your sd card```')
        sent = 1
    if ctx.message.content == ".help sdroot":
        await ctx.send('```Shows what the root of an sd card is```')
        sent = 1
    if ctx.message.content == ".help invite":
        await ctx.send('```Invite commands are: ivan, homebrew, analog, and chill```')
        sent = 1
    if ctx.message.content == ".help ivan":
        await ctx.send('```An invite to internet ivans discord server```')
        sent = 1
    if ctx.message.content == ".help homebrew":
        await ctx.send('```An invite to Nintendo Homebrews discord server```')
        sent = 1
    if ctx.message.content == ".help memes":
        await ctx.send('```Memes are: radeon, snas, uwuham, lazr, local58, pat```')
        sent = 1
    if ctx.message.content == ".help pat":
        await ctx.send('For when someone needs that extra bit of support.')
        sent = 1
    if ctx.message.content == ".help radeon":
        await ctx.send('Type the command :wink:')
        sent = 1
    if ctx.message.content == ".help snas":
        await ctx.send('Type the command :wink:')
        sent = 1
    if ctx.message.content == ".help uwuham":
        await ctx.send('Type the command :wink:')
        sent = 1
    if ctx.message.content == ".help lazr":
        await ctx.send('Type the command :wink:')
        sent = 1
    if ctx.message.content == ".help luma":
       await ctx.send('Shows the different luma versions')
       sent = 1
    if ctx.message.content == ".help sd":
       await ctx.send('Shows the guide to help you with your SD card')
       sent = 1
    if ctx.message.content == ".help ap":
        await ctx.send('```Shows the AP-Patching guide```')
        sent = 1
    if ctx.message.content == ".help ndsforwarders":
        await ctx.send('```Shows the NDS Forwarders guide```')
        sent = 1
    if ctx.message.content == ".help vc":
        await ctx.send('```Shows the guide on how to play old classics on your system```')
        sent = 1
    if ctx.message.content == ".help local58":
        await ctx.send('<@664297659686715403> says: honestly i have no idea what this is')
        sent = 1
    if ctx.message.content == ".help troubleshoot":
        await ctx.send('```Shows how to troubleshoot seedminer based methods```')
        sent = 1
    if ctx.message.content == ".help twlfix":
        await ctx.send('```Shows how to fix the DSiWare from different vantage points```')
        sent = 1
    if sent == 0:
        await ctx.send('```What can I help you with?\n\n assistance\n invite\n memes```')

@client.command()
async def vc(ctx):
    sent = 0
    if ctx.message.content == ".vc 3ds":
        await ctx.send('You can convert your roms to CIA format with this tool: https://mega.nz/#!qnAE1YjC!q3FRHgIAVEo4nRI2IfANHJr-r7Sil3YpPYE4w8ZbUPY \nUsage guide here: http://3ds.eiphax.tech/nsui.html')
        sent = 1
    if ctx.message.content == ".vc wiiu":
        await ctx.send('You can play classics on your wiiu with this tool: https://gbatemp.net/threads/release-uwuvci-injectiine.486781/ \nUsage guide here: https://flumpster.github.io/instructions/index')
        sent = 1
    if sent == 0:
        await ctx.send('Invalid syntax. Options are: 3ds, wiiu.')

@client.command()
async def baninfo(ctx):
    sent = 0
    if ctx.message.content == ".baninfo 3ds":
        await ctx.send('''3DS Bans
Nintendo has shown a marked lack of care about bans on the 3DS lately.
However, such things as piracy and cheating online/cheating in multiplayer games have been known causes for NNID/console bans in the past.
eShop fraud (eg credit card chargebacks) will also get you banned.

You can enable online status and Spotpass/Streetpass as these do not seem to be high risk at this time.''')
        sent = 1
    if ctx.message.content == ".baninfo switch":
        await ctx.send('Bans on the Switch are complicated. Please read this to learn more about the matter: https://nx.eiphax.tech/ban')
        sent = 1
    if sent == 0:
        await ctx.send('Invalid syntax. Options are: 3ds, switch.')
client.run(token)

