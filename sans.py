print('Loading...')
import subprocess
from inspect import cleandoc
from typing import Union
import os
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

bot = commands.Bot(command_prefix=("."), case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))

tokendir = os.path.dirname(os.path.realpath(__file__))
with open(tokendir + "/token.json") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')
    print(f'We have logged in as {bot.user}')

#assistance

@bot.group()
async def guide(ctx):
    '''Links the CFW guide for various consoles'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Options are: 3ds, wiiu, wii, nx')

@guide.command(name="3ds")
async def _3ds(ctx):
    embed = make_embed(
        title="Guide",
        author="Internet Ivan",
        color=0x56238c,
        thumbnail="https://i.imgur.com/CFp51Hb.jpg",
        url="https://www.youtube.com/watch?v=tt1rUcng4OU",
        description="Guide on how to install B9S on your 3ds"
    )

    await ctx.send(embed=embed)

@guide.command()
async def wiiu(ctx):
    embed = make_embed(
        title="Guide",
        author="Nintendo Homebrew",
        color=0x2ddde3,
        thumbnail="https://i.imgur.com/CVSu1zc.png",
        url="https://wiiu.hacks.guide/",
        description="A complete Wii U custom firmware + coldboothax guide."
    )

    await ctx.send(embed=embed)

@guide.command(aliases=("nx", "ns"))
async def switch(ctx):
    embed = make_embed(
        title="Guide",
        author="Nintendo Homebrew",
        color=0xff0000,
        thumbnail="https://i.imgur.com/CVSu1zc.png",
        url="https://nh-server.github.io/switch-guide/",
        description="A Switch guide from stock to Atmosphere."
    )

    await ctx.send(embed=embed)

@guide.command()
async def wii(ctx):
    embed = make_embed(
        title="Guide",
        author="RiiConnect 24",
        color=discord.Color.default(),
        thumbnail="https://i.imgur.com/KI6IXmm.png",
        url="https://wii.guide/",
        description="A complete Wii custom firmware guide"
    )

    await ctx.send(embed=embed)

@bot.group()
async def what(ctx):
    '''Links the What? pages for various consoles'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Options are: 3ds, switch, ns, nx')
        
@what.command(name="3ds")
async def _3ds(ctx):
    embed = make_embed(
        title="What?",
        color=0x12e6b4,
        url="https://3ds.eiphax.tech/what",
        description="Confused? Click the link above, it'll show you some basic things about the 3DS and CFW"
    )
        
    await ctx.send(embed=embed)
        
@what.command(aliases=("ns", "nx"))
async def switch(ctx):
    embed = make_embed(
        title="What?",
        color=0x006f9e,
        url="https://nx.eiphax.tech/nutshell.html",
        description="Confused? Click the link above, it'll show you some basic things about the Switch and CFW"
    )
    
    await ctx.send(embed=embed)


@bot.command(aliases=["ctrtransfer"])
async def ctr(ctx):
    '''Link the guide for a CTRtransfer'''
    embed = make_embed(
        title="CTRTransfer",
        author="Nintendo Homebrew",
        color=discord.Color.orange(),
        thumbnail="https/nintendohomebrew.com/pics/nhplai.png",
        url="https://3ds.hacks.guide/ctrtransfer",
        description="How to do the 11.5.0-38 ctrtransfer"
    )

    await ctx.send(embed=embed)

@bot.command(aliases=["browserhack"])
async def browserhax(ctx):
    '''Links the guide for BrowserHax2020'''
    embed = make_embed(
        title="Browserhax",
        author="Nintendo Homebrew",
        color=discord.Color.blue(),
        thumbnail="https://3ds.eiphax.tech/pic/browserhaxfriends.png",
        url="https://3ds.hacks.guide/homebrew-launcher-(browserhax-2020)",
        description="A guide on how to do BrowserHax 2020 for getting CFW on your 3DS"
    )

    await ctx.send(embed=embed)

@bot.command()
async def fredtool(ctx):
    '''Link the guide for Fredtool'''
    embed = make_embed(
        title="Fredtool",
        author="3ds.hacks.guide",
        color=discord.Color.orange(),
        url="https://3ds.hacks.guide/installing-boot9strap-(fredtool).html",
        description="A guide on how to install CFW on your 3ds with the fredtool method"
    )
    await ctx.send(embed=embed)


@bot.group()
async def soundhax(ctx):
    '''Link the guide for SoundHax'''
    if ctx.invoked_subcommand is None:
        await ctx.send('What soundhax would you like? hbl, b9s')

@soundhax.command()
async def hbl(ctx):
    embed = make_embed(
        title="Soundhax HBL",
        author="3ds.hacks.guide",
        color=discord.Color.red(),
        url="https://3ds.hacks.guide/homebrew-launcher-(soundhax)",
        description="A guide on getting the HBL through Soundhax"
    )
    await ctx.send(embed=embed)

@soundhax.command()
async def b9s(ctx):
    embed = make_embed(
        title="Soundhax HBL",
        author="3ds.hacks.guide",
        color=discord.Color.red(),
        url="https://3ds.hacks.guide/installing-boot9strap-(soundhax)",
        description="A guide on installing Boot9strap on your 3ds through Soundhax"
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["finalize"])
async def finalizing(ctx):
    '''Links 3DS Finalizing Setup'''
    embed = make_embed(
        name="3ds.hacks.guide Finalizing Setup",
        color=0x2aa8a0,
        description="[Finalizing Setup](https://3ds.hacks.guide/finalizing-setup)",
    )
    await ctx.send(embed=embed)
	
@bot.command()
async def atob(ctx):
    '''Links the A9LH to B9S guide'''
    embed = make_embed(
        title="Upgrading a9lh to b9s",
        author="NH and Friends",
        color=0xde3700,
        thumbnail="https://nintendohomebrew.com/pics/nhplai.png",
        url="https://3ds.hacks.guide/a9lh-to-b9s",
        description="A guide for upgrading your device from arm9loaderhax to boot9strap."
    )
    await ctx.send(embed=embed)

@bot.command()
async def troubleshoot(ctx):
    '''Links the 3DS CFW troubleshooting guide'''
    embed = make_embed(
        title="Troubleshoot",
        color=discord.Color.purple(),
        url="https://3ds.eiphax.tech/issues.html",
        description="A simple troubleshooting guide for common CFW and homebrew installation issues when using popular recent 3DS hacking methods."
    )

    await ctx.send(embed=embed)

@bot.command()
async def emptysd(ctx):
    '''Shows what to do when you've lost the sd contents with CFW installed.'''
    embed = make_embed(
        title="",
        color=0xc99400,
        description="If you have lost the contents of your SD card with CFW, you will need in SD root: boot.firm and boot.3dsx from luma3ds [latest release](https://github.com/LumaTeam/Luma3DS/releases) Then repeat [finalizing setup](https://3ds.hacks.guide/finalizing-setup)"
    )

    await ctx.send(embed=embed)

@bot.command()
async def lumacheck(ctx):
    '''Instructions on how to check a 3DS luma version'''
    embed = make_embed(
        title="How to check your Luma version",
        color=0x2aa8a0,
        description=cleandoc("""
            1. Power off your console
            2. Press and hold the SELECT button, then press power while still holding SELECT
            3. Send a picture of the Luma configuration
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def notbricked(ctx):
    ''''Don't worry, you haven't broken it'''
    embed = discord.Embed(
        title="No you are not bricked",
        description=cleandoc("""
            If your power LED turns on and off after you installed b9s, you are not bricked and are just missing a file called boot.firm in the root of your SD card to fix the issue
            1. Check you inserted the SD card in your console
            2. Place/replace the file, downloading it from [here](https://github.com/LumaTeam/Luma3DS/releases).
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def lumabug(ctx):
    '''Show instructions to fix the luma black screen bug'''
    await ctx.send('Luma Black Screen Bug If you have Luma3DS and your console is stuck on a black screen after you power it on, follow these steps:\n 1. Power off the console.\n 2. Take out any game cartridge, but leave the SD card in.\n 3. Power on the console.\n 4. Leave the console open and powered on for 10-15 minutes. Do not touch the console during this time.\n If the console boots successfully in that time, the bug is now fixed and is unlikely to happen again. If the console still fails to boot to home menu, come back and ask for more help. Mention that you have already tried the Luma black screen process.')

@bot.command()
async def pinkscreen(ctx):
    '''No, you didn't break it this time, either'''
    embed = discord.Embed(
        title="No, it's not broken",
        description=cleandoc("""
            If you try to install CFW but get a pink screen in the process, there are two things that might've happened.
            1. You already have CFW.
            2. You messed up the file placement somewhere, and need to change it.
            To check if you have CFW, turn off the console, then press and hold select and boot the system while still holding select.
            If you boot into Luma, then you have it.
            If not, you messed up file placement. Did you place things in the [ROOT](https://cdn.discordapp.com/attachments/754753360132833431/757705163220713632/image0.png) of the sd card?
            If you booted into luma, you should try [finalizing](https://3ds.hacks.guide/finalizing-setup) it now, as you probably don't have any software right now.
        """)
    )
    
    await ctx.send(embed=embed)

@bot.command()
async def sdlock(ctx):
    '''Instructions on how to disable an SD write protect switch'''
    embed = make_embed(
        title="Disable write protection on an SD Card",
        color=discord.Color.default(),
        image="https://i.imgur.com/R64mbmG.png",
        description=cleandoc("""
            This switch on the SD Card should be facing upwards, as in this photo. Otherwise, your device will refuse to write to it.
            *If it is write locked, your console and other applications may behave unexpectedly.*
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def sdroot(ctx):
    '''A visual guide to what in the heck the root means'''
    embed = make_embed(
        title="",
        color=discord.Color.default(),
        image="https://cdn.discordapp.com/attachments/754753360132833431/757705163220713632/image0.png"
    )

    await ctx.send(embed=embed)

@bot.command(name="7zip")
async def _7zip(ctx):
    '''Links 7-zip download'''
    embed = make_embed(
        title="7Zip Info",
        color=0x2aa8a0,
        description="WinRAR isn't a very good archiving utility. You should use 7-Zip instead \n which can be downloaded [here](https://www.7-zip.org)."
    )
    await ctx.send(embed=embed)
    
@bot.command(aliases=["redscr"])
async def boot3dsx(ctx):
    '''Links boot.3dsx'''
    embed = make_embed(
        title="The 3DS Homebrew Launcher",
        color=0x262626,
        description="[boot.3dsx](https://github.com/fincs/new-hbmenu/releases/download/v2.1.0/boot.3dsx)"
    )
    await ctx.send(embed=embed)
    
@bot.command()
async def luma(ctx, version):
    '''Links the download to various Luma3DS versions'''
    luma_versions = {
        "latest": "https://github.com/LumaTeam/Luma3DS/releases/latest",
        "7.0.5": "https://github.com/LumaTeam/Luma3DS/releases/tag/v7.0.5",
        "7.1": "https://github.com/LumaTeam/Luma3DS/releases/tag/v7.1"
    }
    try:    await ctx.send(luma_versions[version])
    except: await ctx.send('```What luma version would you like?\n\n latest\n 7.0.5\n 7.1```')

@bot.command()
async def bootnds(ctx):
    await ctx.send('https://github.com/zoogie/b9stool/releases/download/v6.0.0/release_6.0.0.zip')

@bot.command()
async def cartinstall(ctx):
    '''Links the CartInstall guide'''
    embed = make_embed(
        title="CartInstall",
        author="Internet Ivan",
        color=discord.Color.default(),
        thumbnail="https://i.imgur.com/CFp51Hb.jpg",
        url="https://youtu.be/pzbfHQ6uTcU",
        description="How to install 3DS cartridges to the SD card"
    )

    await ctx.send(embed=embed)

@bot.command()
async def dump(ctx, console):
    '''Links the dumping guide for various game consoles'''
    dump_guides = {
        "ds": "https://youtu.be/x-Et2zkl3Ek",
        "nx": "https://suchmememanyskill.github.io/guides/switchdumpguide/",
        "wii": "https://wii.guide/dump-games",
        "3ds": "https://youtu.be/b1Ng-b0fnpg",
        "wiiu": "https://wiiu.hacks.guide/#/dump-games",
        "vwii": "https://wiiu.hacks.guide/#/dump-wii-games"
    }

    try:    await ctx.send(dump_guides[console.lower()])
    except: await ctx.send('Options are: 3ds, ds, wiiu, vwii, wii, nx')

@bot.command()
async def ftp(ctx):
    '''Links FTPD guide'''
    embed = make_embed(
        title="FTP Guide",
        author="Krieg",
        color=0x2aa8a0,
        url="https://3ds.eiphax.tech/ftp.html",
        description="A guide on how to set up FTP on your 3ds.",
    )
    await ctx.send(embed=embed)

@bot.command()
async def twlmenu(ctx):
    '''TWiLight Menu++ setup instructions'''
    await ctx.send('https://www.youtube.com/watch?v=07ZMSrrZwCQ')

@bot.command()
async def twlfix(ctx, mode):
    '''Instructions for fixing a broken TWLNand'''
    twlfix_links = {
        "cfw": "TWLFix-CFW/releases",
        "3ds": "TWLFix-3DS/releases",
        "stock": "TWLFix/wiki/Instructions"
    }
    try:    await ctx.send(f"```Use this tool to fix the dsiware on your 3ds!``` <https://github.com/MechanicalDragon0687/{twlfix_links[mode.lower()]}/>, please note that you must do a system update after the process has finished'")
    except: await ctx.send('```What twlfix would ya like? cfw, 3ds, stock```')

@bot.command()
async def ndsforwarders(ctx):
    '''Instructions for using NDS Forwarders'''
    await ctx.send('https://gbatemp.net/threads/nds-forwarder-cias-for-your-home-menu.426174/')

@bot.command()
async def ap(ctx):
    '''Anti-Piracy patching guide for DS titles'''
    await ctx.send('https://glazedbelmont.github.io/appatching/')

@bot.command(aliases=["sderrors"])
async def sd(ctx):
    '''Link a guide to test SD cards for failures'''
    await ctx.send('<https://3ds.eiphax.tech/sd.html>')

@bot.command(aliases=["formatsd"])
async def sdformat(ctx):
    embed = make_embed(
        title="**Common SD Formatting tools**",
        color=0x2aa8a0,
        description=cleandoc("""
            Windows-[guiformat](http://ridgecrop.co.uk/index.htm?guiformat.htm)
            Linux-[gparted](https://gparted.org/download.php) + [dosfstools](https://github.com/dosfstools/dosfstools)
            MacOS-[Disk Utility](https://support.apple.com/guide/disk-utility/format-a-disk-for-windows-computers-dskutl1010)
            
            MacOS: Always select "MS-DOS (FAT)", even if the card is larger than 32GB.
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def db(ctx, console):
    '''Links 3DS title database'''
    if console.lower() == "3ds":
        embed = make_embed(
            title="3DS Database",
            url="http://3dsdb.com/",
            color=discord.Color.dark_orange(),
            description="3DS database for game releases."
        )
        await ctx.send(embed=embed)
    else:
        raise commands.BadArgument

@bot.command()
async def vc(ctx):
    '''Link a guide for Virtual Console injects'''
    sent = 0
    if str(ctx.message.content).startswith(".vc 3ds"):
        embed=discord.Embed(title="Virtual Console Injects for 3DS", color=discord.Color(0xab1f1f))
        embed.set_author(name="Asdolo")
        embed.set_thumbnail(url="https://i.imgur.com/rHa76XM.png")
        embed.url = "https://mega.nz/#!qnAE1YjC!q3FRHgIAVEo4nRI2IfANHJr-r7Sil3YpPYE4w8ZbUPY"
        embed.description = "The recommended way to play old classics on your 3DS. Usage guide [here](http://3ds.eiphax.tech/nsui.html)."
        await ctx.send(embed=embed)
        sent = 1
    if str(ctx.message.content).startswith(".vc wiiu"):
        embed=discord.Embed(title="Virtual Console Injects for Wii U", color=discord.Color(0x3691b5))
        embed.set_author(name="NicoAICP")
        embed.set_thumbnail(url="https://gbatemp.net/data/avatars/l/404/404553.jpg")
        embed.url = "https://gbatemp.net/threads/release-uwuvci-injectiine.486781/"
        embed.description = "The recommended way to play old classics on your Wii U. Usage guide [here](https://flumpster.github.io/instructions/index)."
        await ctx.send(embed=embed)
        sent = 1
    if sent == 0:
        await ctx.send('Invalid syntax. Options are: 3ds, wiiu.')

@bot.command()
async def cfwuses(ctx, console):
    '''Link a page showing some things you can use CFW for'''
    cfwuses_images = {
        "3ds": "https://3ds.eiphax.tech/tips.html",
        "wiiu": "https://cdn.discordapp.com/attachments/754753360132833431/757744237440794654/wiiu_cfw.PNG",
        "nx": "https://cdn.discordapp.com/attachments/744815170626519062/758814416992075816/Screenshot_20200924-151725_Discord.jpg"
    }
    try:    await ctx.send(cfwuses_images[console.lower()])
    except: await ctx.send('Options are: 3ds, wiiu, nx')

@bot.group()
async def baninfo(ctx):
    '''Show information about Ban Risk on various consoles'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid syntax. Options are: 3ds, wiiu, nx, ns, switch, retro')

@baninfo.command(name="3ds")
async def _3ds(ctx):
    embed = discord.Embed(
        title="**3DS Bans**",
        description=cleandoc("""
            Nintendo has shown a marked lack of care about bans on the 3DS lately.
            However, such things as piracy and cheating online/cheating in multiplayer games have been known causes for NNID/console bans in the past.
            eShop fraud (eg credit card chargebacks) will also get you banned.
            You can enable online status and Spotpass/Streetpass as these do not seem to be high risk at this time.
        """)
    )
    
    await ctx.send(embed=embed)

@baninfo.command()
async def wiiu(ctx):
    embed = discord.Embed(
        title="**WiiU Bans**",
        description=cleandoc("""
            Just like 3DS, Nintendo has shown a marked lack of care about bans on the Wii U lately.
            However, such things as piracy and cheating online/cheating in multiplayer games have been known causes for NNID/console bans in the past.
            eShop fraud (eg credit card chargebacks) will also get you banned.
            You can enable online status and Spotpass/Streetpass as these do not seem to be high risk at this time.
        """)
    )
    
    await ctx.send(embed=embed)

@baninfo.command(aliases=("nx", "ns"))
async def switch(ctx):
    embed = discord.Embed(
        title="**Switch Bans**",
        thumbnail="https://eiphax.tech/assets/gunther.png",
        url="https://nx.eiphax.tech/ban",
        description="Bans on the Switch are complicated. Please click the embed header link and read the linked page to learn more."
    )

    await ctx.send(embed=embed)
    
@baninfo.command()
async def retro(ctx):
    embed = discord.Embed(
        title="**Wii and DS Bans**",
        description=cleandoc("""
            Retro Nintendo servers are no longer hosted by Nintendo themselves. For the most part they are hosted by Wiimfi. This does not, however, mean that you are free from getting banned.
            Bans are usually for hacking in games, or having inappropriate names.
            For a list of current bans and reasons, check [here](https://wiimmfi.de/show-bans).
            And as a forewarning, do not contact Wiim himself for a ban removal. This may in fact prolong your ban.
        """)
    )
    
    await ctx.send(embed=embed)

@bot.command(aliases=["cbhcrules"])
async def cbhc(ctx):
    '''Show some CBHC rules that should be followed'''
    embed = discord.Embed(
        title="CBHC Rules:",
        description=cleandoc("""
            - The DS game has to be legitimately installed from the eShop!
            - Don’t format the system while CBHC is installed!
            - Don’t delete the user account that bought the DS VC game!
            - Don’t re-install the same game using WUP Installer or from the eShop!
            - Don’t install Haxchi over CBHC! (You will not brick, but it will cause a boot-loop! Hold A when booting to access the Homebrew Launcher and uninstall CBHC.)
            - Don’t uninstall the DS Virtual Console game without properly uninstalling CBHC first! <https://wiiu.hacks.guide/#/uninstall-cbhc>
            - Don’t move the DS Virtual Console game to a USB drive!
        """)
    )
    
    await ctx.send(embed=embed)


#memes

@bot.command()
async def halp(ctx):
    '''Halp'''
    await ctx.send("no")
    
@bot.command()
async def pat(ctx):
    '''*pats*'''
    await ctx.send("https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819")

@bot.command()
async def lazr(ctx):
    '''bottom gear mates'''
    await ctx.send('YOU SODDING TICTAC')

@bot.command()
async def radeon(ctx):
    '''can relate'''
    await ctx.send('you ever just want to sleep? for like a week?')

@bot.command()
async def uwuham(ctx):
    '''something is very wrong here, get the node.js juice'''
    await ctx.send('guys somethings wrong with uwuham hes using python')

@bot.command()
async def mega97(ctx):
    '''Bro it makes so sense'''
    await ctx.send("y'all ever just want to 🏱︎☜︎☞︎☟︎𓋴𓂧𓈖𓋴𓊪𓅱𓄿👌︎✞︎👍︎👎︎𓅓𓎡𓈖𓄿𓊃☜︎🕈︎✌︎☪︎💧︎☜︎👎︎☞︎✞︎𓋴𓆑𓂧𓈖☟︎☠︎☟︎☝︎☞︎👍︎✠︎☞︎☝︎☝︎☞︎👍︎")

@bot.command(aliases=["siconoo"])
async def siconove(ctx):
    '''sodding tictac'''
    await ctx.send("MAKE YOUR OWN COMMAND YOU SODDING TICTAC")
	
@bot.command()
async def snas(ctx):
    '''fortnite battle royale'''
    await ctx.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

@bot.command()
async def brick(ctx):
    '''why does this even exist (note from lazr: it exists because yes)'''
    await ctx.send('nah fuck you :wink:')

#bot stuff

@bot.command()
async def sans(ctx):
    '''Links the github repo for Sans'''
    embed = make_embed(
        title="Sans",
        author="Maintained by Lazr, Radeon, and UwUham",
        color=discord.Color.green(),
        thumbnail="https://i.imgur.com/AkOLH6q.png",
        url="https://github.com/Lazr1026/Sans",
        description="Sans, The discord bot that is kinda useful!"
    )

    await ctx.send(embed=embed)

@bot.command()
async def contributors(ctx):
    '''Lists currect Sans contributors'''
    embed = discord.Embed(
        title="List of current Sans contributors",
        description=cleandoc("""
            Lazr1026 - Creator and programmer
            476MHz (Radeon) - Programmer
            Uwuham - Telling us discord.js is better
            Techmuse - PR'd useful shit
            Gnome! - Cleaned everything up massively
            ItsPizzaTime1501 - Helped with proper licensing
            bleck9999 - (I'm not sure what bleck did, feel free to edit this part - Meganium97)
            Maretu (ray) - Fixed our terrible grammar
            Meganium97 (Dire) - Idk, what are you asking me for?
        """)
    )
    
    await ctx.send(embed=embed)
    
@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! Latency is {int(bot.latency * 1000)} ms!')

#other

@bot.command()
async def listhelpers(ctx):
    '''Lists helpers in Internet Ivan's discord guild'''
    embed = make_embed(
        title="Here are our helpers:",
        color=0x20b339,
        description=cleandoc("""
            **__3DS__**
            <@554832528238968883>
            <@578245729060126730>
            <@504564321716666368>
            <@334102523365425163>
	    <@395524987315814400>
            **__Wii U__**
            <@664297659686715403>
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def liststaff(ctx):
    '''Lists staff in Internet Ivan's discord guild'''
    embed = make_embed(
        title="Here is a list of our staff:",
        color=0x132e91,
        description=cleandoc("""
            **__Owner__**
            <@505793682297978900>
            **__Admin__**
            <@554832528238968883>
            <@664297659686715403>
        """)
    )
    await ctx.send(embed=embed)


@bot.command(aliases=["pfp"])
async def profile(ctx, user: discord.User):
    '''Fetch a user's profile icon'''
    await ctx.send(f"Profile image for user: {user.name}")
    pfp = user.avatar_url
    await ctx.send(pfp)

# Gnome: Hey look, it is my code :GWcorbintopkek:

@bot.command()
@commands.has_any_role('Owner', 'Admin')
async def proxyuser(ctx, user: Union[discord.Member, discord.User, int, str], *, message):
    '''bulshit, BULLSHIT!'''
    await ctx.message.delete()
    if isinstance(user, int):
        try:    user = await self.bot.fetch_user(user)
        except: user = str(user)
    if isinstance(user, str):
        name = user
        avatar = "https://cdn.discordapp.com/avatars/689564772512825363/f05524fd9e011108fd227b85c53e3d87.png"
    else:
        name = user.display_name
        avatar = user.avatar_url
    if "@everyone" in message or "@here" in message:
        message = message.replace("@everyone", "everyone")
        message = message.replace("@here", "here")
    webhooks = await ctx.channel.webhooks()
    if len(webhooks) == 0:
        webhook = await ctx.channel.create_webhook(name="Webhook for bullshit")
        await webhook.send(message, username=name, avatar_url=avatar)
        await webhook.delete()
    else:
        webhook = webhooks[0]
        await webhook.send(message, username=name, avatar_url=avatar)

@bot.group()
async def neworold(ctx):
    '''Shows which version of console you have'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid syntax. Options are: 3ds, wii, nx, ns, switch')
        
@neworold.command(name="3ds")
async def _3ds(ctx):
    embed = make_embed(
        title="**3DS Versions**",
        color=discord.Color.default(),
        image="https://sagamer.co.za/wp-content/uploads/2014/10/New-3DS-vs-3DS-SA-Gamer.jpg",
        description=cleandoc("""
            Telling apart a New3DS from an old one is pretty simple. All you need to do is look above the abxy buttons.
            If there is a c-stick above the abxy buttons, then you have a New3DS.
            If there isn't, then you have an old 3DS.
        """)
    )

    await ctx.send(embed=embed)
    
@neworold.command(aliases=("nx","ns"))
async def switch(ctx):
    embed = make_embed(
        title="**Switch Versions**",
        color=discord.Color.default(),
        image="https://www.imore.com/sites/imore.com/files/styles/large/public/field/image/2019/08/switch-packaging-comparison.jpg",
        description=cleandoc("""
            Telling apart a new switch from an old one isn't like how you would do it with the 3DS.
            One way is by looking at the serial numbers on the switch. These can tell you exactly which version you have.
            If you just want a generalization of which version you have, just look at the box.
        """)
    )

    await ctx.send(embed=embed)

@neworold.command()
async def wii(ctx):
    embed = make_embed(
        title="**Wii Versions**",
        color=discord.Color.default(),
        image="https://retrogamebuyer.com/wp-content/uploads/2020/03/RVL-001-vs-101.png?ezimgfmt=rs:372x186/rscb1/ng:webp/ngcb1",
        description=cleandoc("""
            Telling apart the different Wii versions is by far the easiest.
            If your Wii has slots for Gamecube memory cards and controllers, then you have an original Wii
            If it doesn't, then you have a newer one.
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx, invite):
    '''Shows the invites for various discord guilds (ivan, homebrew, analog, chill)'''
    invites = {
        "ivan": "NM85JqJ",
        "chill": "eTS6yym",
        "analog": "7bXpJSh",
        "homebrew": "C29hYvh"
    }
    try:    await ctx.send(f"https://discord.gg/{invites[invite.lower()]}")
    except: await ctx.send('Options are: ivan, homebrew, analog, chill.')

@bot.command()
async def serial(ctx):
    '''Shows how to check your Switch's serial number'''
    embed = make_embed(
        title="**Switch Serial Number**",
        color=discord.Color.default(),
        image="https://i.imgur.com/03NfeFN.png",
        description=cleandoc("""
           Dont know where your switch serial number is? Look at this image to help ya out
        """)
    )

    await ctx.send(embed=embed)

@bot.command()
async def r4(ctx):
    '''R4? that sounds like a kind of breakfast cereal (tells what an R4(i) cartridge is)'''
    await ctx.send('An R4 is a Flashcart that can or cannot be used for ntrboot (unbrick and cfw installation tool I guess you can call it). Its also used to play gaems (hopefully dumped from carts).')

@bot.command()
async def meta(ctx):
    '''meta? don't you mean off-topic 2?'''
    await ctx.send('you seem to be in <#759902836116160532>')

#admin stuff

@bot.command(aliases=["yeet"])
@commands.has_any_role('Owner', 'Staff', 'Admin')
async def ban (ctx, member: discord.User = None, reason="[no reason specified]"):
    '''does what it says on the tin'''
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself.")
        return
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await ctx.guild.ban(member, reason=reason, delete_message_days=0)
    await ctx.channel.send(f"{member} has been b&. 👍")
    await member.send(message)
    
@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin', 'Helper')
async def kick(ctx, member: discord.Member, *, reason=0):
    '''does what it says on the tin'''
    await member.kick(reason=reason, delete_message_days=0)
    send = f"user {member.name} has been kicked."
    await ctx.send(send)

@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin', 'Helper')
async def say(ctx, message):
    '''does what it says on the tin (helpers+)'''
    await ctx.message.delete()
    await ctx.send(ctx.message.content[5:])

@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin',)
async def update(ctx):
    await ctx.send("Updating code. The bot will be down for roughly 15 seconds.")
    subprocess.run(['bash', '/home/lazr/Documents/Sans/recovery/sans.sh'])
    
@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin')
async def reboot(ctx):
    await ctx.send("Rebooting bot. Bot will be down for a few seconds.")
    subprocess.run(['bash', '/home/lazr/Documents/Sans/recovery/reboot.sh'])

#piracy related things

@bot.command()
async def amiapirate(ctx):
    '''Explains what piracy is and how it's bad'''
    await ctx.send("https://3ds.eiphax.tech/piracy")
    
@bot.command(aliases=["r11"])
async def pirate(ctx):
    '''oi buy your games m8 (tells why piracy is bad)'''
    await ctx.send('We do not support nor condone piracy as it is\n 1. Against Discord TOS\n 2. It is illegal, buy your damn games')

@bot.command()
async def pirate2(ctx):
    '''oi m8 buy your gams (alternative to pirate)'''
    await ctx.send('yeah you just need to go to the eShop, put in the magic numbers on your credit card, and then go and press download on the game you want.')
    
bot.run(token)
