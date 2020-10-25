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

bot = commands.Bot(command_prefix = '.')

tokendir = os.path.dirname(os.path.realpath(__file__))
with open(tokendir + "/token") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')
    print(f'We have logged in as {bot.user}')

@bot.command()
async def amiapirate(ctx):
    '''Explains what piracy is and how it is bad'''
    await ctx.send("https://3ds.eiphax.tech/piracy")

@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! Latency is {int(bot.latency * 1000)} ms!')

@bot.command()
async def pat(ctx):
    '''*pats*'''
    await ctx.send("https://imgur.com/gallery/WyMHuyL")

@bot.command()
async def pirate2(ctx):
    '''oi m8 buy your gams (alternative to pirate)'''
    await ctx.send('yeah you just need to go to the eShop, put in the magic numbers on your credit card, and then go and press download on the game you want.')

@bot.command(aliases=["finalize"])
async def finalizing(ctx):
    '''Links 3DS Finalizing Setup'''
    embed = make_embed(
        name="3ds.hacks.guide Finalizing Setup",
        color=0x2aa8a0,
        description="[Finalizing Setup](https://3ds.hacks.guide/finalizing-setup)",
    )

    await ctx.send(embed=embed)

@bot.command(name="7zip")
async def _7zip(ctx):
    '''Links 7-zip download'''
    embed = make_embed(
        title="7Zip Info",
        color=0x2aa8a0,
        description="WinRAR is not a very good archiving utility. You should use 7-Zip instead \n which can be downloaded [here](https://www.7-zip.org)."
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
async def listhelpers(ctx):
    '''Lists helpers in Internet Ivan's discord guild'''
    embed = make_embed(
        title="Here is our helpers:",
        color=0x20b339,
        description=cleandoc("""
            **__3DS__**
            <@554832528238968883>
            <@578245729060126730>
            <@504564321716666368>
            <@505832724959985666>
            <@334102523365425163>
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
            <@505832724959985666>
        """)
    )
    await ctx.send(embed=embed)

@bot.command()
async def ftp(ctx):
    '''Links FTPD guide'''
    embed = make_embed(
        title="FTP Guide",
        author="Kreig",
        color=0x2aa8a0,
        url="https://3ds.eiphax.tech/ftp.html",
        description="A guide on how to set up FTP on your 3ds, Note 3ds and switch are basically the same process",
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
        author="NH Discord Server",
        color=0xff0000,
        thumbnail="https://i.imgur.com/CVSu1zc.png",
        url="https://nh-server.github.io/switch-guide/",
        description="A Switch guide from stock to Atmosphere."
    )

    await ctx.send(embed=embed)

@guide.command()
async def wii(ctx):
    embed = make_embed(
        author="RiiConnect24",
        color=0xdedede,
        thumbnail="https://i.imgur.com/KI6IXmm.png",
        description="A complete original Wii softmod guide."
    )

    await ctx.send(embed=embed)

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

@bot.command(aliases=["browserhack"])
async def browserhax(ctx):
    '''Links the guide for BrowserHax2020'''
    embed = make_embed(
        title="Browserhax",
        author="Nintendo Homebrew and Friends",
        color=discord.Color.blue(),
        thumbnail="https://3ds.eiphax.tech/pic/browserhaxfriends.png",
        url="https://3ds.hacks.guide/homebrew-launcher-(browserhax-2020)",
        description="A guide on how to do BrowserHax 2020 for getting CFW on your 3DS"
    )

    await ctx.send(embed=embed)

@bot.command(aliases=["ctrtransfer"])
async def ctr(ctx):
    '''Link the guide for a CTRtransfer'''
    embed = make_embed(
        title="CTRTransfer",
        author="Nintendo Homebrew and Friends",
        color=discord.Color.orange(),
        thumbnail="https/nintendohomebrew.com/pics/nhplai.png",
        url="https://3ds.hacks.guide/ctrtransfer",
        description="How to do the 11.5.0-38 ctrtransfer"
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
        description="A guide on how to install CFW on your 3ds with the fredtool method")

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

@bot.command()
async def atob(ctx):
    '''Link the A9LH to B9S guide'''
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
    '''Link the 3DS CFW troubleshooting guide'''
    embed = make_embed(
        title="Troubleshoot",
        color=discord.Color.purple(),
        url="https://3ds.eiphax.tech/issues.html",
        description="A simple troubleshooting guide for common CFW and homebrew installation issues when using popular recent 3DS hacking methods."
    )

    await ctx.send(embed=embed)

@bot.command()
async def cartinstall(ctx):
    '''Link the CartInstall guide'''
    embed = make_embed(
        title="CartInstall",
        author="Internet Ivan",
        color=discord.Color.default(),
        thumbnail="https://i.imgur.com/CFp51Hb.jpg",
        url="https://youtu.be/pzbfHQ6uTcU",
        description="How to install 3DS cartridges to the SD card"
    )

    await ctx.send(embed=embed)

@bot.command(aliases=["godmode9"])
async def gm9(ctx):
    '''Link the GodMode9 usage guide'''
    embed = make_embed(
        title="GodMode9 Usage",
        author="NH & Friends",
        color=0x851111,
        thumbnail="https://nintendohomebrew.com/pics/nhplai.png",
        url="https://3ds.hacks.guide/godmode9-usage",
        description="GodMode9 usage guide"
    )

    await ctx.send(embed=embed)

@bot.command()
async def dump(ctx, console):
    '''Link the dumping guide for various game types'''
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
async def invite(ctx, invite):
    '''Show the invites for various discord guilds'''
    invites = {
        "ivan": "NM85JqJ",
        "chill": "7ECUWDp",
        "analog": "7bXpJSh",
        "homebrew": "C29hYvh"
    }

    try:    await ctx.send(f"https://discord.gg/{invites[invite.lower()]}")
    except: await ctx.send('Options are: ivan, homebrew, analog, chill.')

@bot.command()
async def luma(ctx, version):
    '''Link the download to various Luma3DS versions'''
    luma_versions = {
        "latest": "https://github.com/LumaTeam/Luma3DS/releases/latest",
        "7.0.5": "https://github.com/LumaTeam/Luma3DS/releases/tag/v7.0.5",
        "7.1": "https://github.com/LumaTeam/Luma3DS/releases/tag/v7.1"
    }
    try:    await ctx.send(luma_versions[version])
    except: await ctx.send('```What luma version would you like?\n\n latest\n 7.0.5\n 7.1```')

@bot.command(aliases=["r11"])
async def pirate(ctx):
    '''oi buy your games m8 (tells why piracy is bad)'''
    await ctx.send('We do not support nor condone piracy as it is\n 1. Against Discord TOS\n 2. It is illegal, buy your damn games')

@bot.command()
async def lumacheck(ctx):
    '''Instructions to check a 3DS luma version'''
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
        image="https://cdn.discordapp.com/attachments/754753360132833431/757705163220713632/image0.png"
    )

    await ctx.send(embed=embed)

@bot.command()
async def r4(ctx):
    '''R4? that sounds like a kind of breakfast cereal (tells what an R4(i) cartridge is)'''
    await ctx.send('An R4 is a Flashcart that can or cannot be used for ntrboot (unbrick and cfw installation tool I guess you can call it). Its also used to play gaems (hopefully dumped from carts).')

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

@bot.command()
async def tinydb(ctx):
    '''Links eiphax's 3DS tinydb'''
    await ctx.send('https://tinydb.eiphax.tech/')

@bot.command()
async def meta(ctx):
    '''meta? don't you mean off-topic 2?'''
    await ctx.send('you seem to be in <#759902836116160532>')

@bot.command()
async def cbhc(ctx):
    '''Show some CBHC rules that should be followed'''
    await ctx.send(cleandoc("""
        CBHC Rules:
        - The DS game has to be legitimately installed from the eShop!
        - Don’t format the system while CBHC is installed!
        - Don’t delete the user account that bought the DS VC game!
        - Don’t re-install the same game using WUP Installer or from the eShop!
        - Don’t install Haxchi over CBHC! (You will not brick, but it will cause a boot-loop! Hold A when booting to access the Homebrew Launcher and uninstall CBHC.)
        - Don’t uninstall the DS Virtual Console game without properly uninstalling CBHC first! <https://wiiu.hacks.guide/#/uninstall-cbhc>
        - Don’t move the DS Virtual Console game to a USB drive!
        """)
    )

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
async def nospace(ctx):
    '''Instructions on making a 3DS nand backup without enough space'''
    await ctx.send('How to make a NAND backup without enough space on your sd card:\n 1. Copy the Nintendo 3DS and the DCIM folder (if you have it) to your computer, then delete them from your SD CARD.\n 2. Boot into GodMode9 and perform the backup again. Once it’s done power off your system.\n 3. Copy all the files in the gm9/out folder on your sd card to a place on your pc. Then delete those files from the SD CARD.\n 4. Copy the Nintendo 3DS and DCIM folder (if you had it) back to your sd card and delete it from your computer.')

@bot.command(aliases=["sderrors"])
async def sd(ctx):
    '''Link a guide to test SD cards for failures'''
    await ctx.send('How to check your sd card for errors:\n <https://3ds.eiphax.tech/sd.html>')

@bot.command(aliases=["pfp"])
async def profile(ctx, user: discord.User):
    '''Fetch a user's profile icon'''
    await ctx.send(f"Profile image for user: {user.name}")
    pfp = user.avatar_url
    await ctx.send(pfp)

@bot.command()
async def radeon(ctx):
    '''can relate'''
    await ctx.send('you ever just want to sleep? for like a week?')

@bot.command()
async def uwuham(ctx):
    '''something is very wrong here, get the node.js juice'''
    await ctx.send('guys somethings wrong with uwuham hes using python')

@bot.command()
async def credits(ctx):
    '''stuff like this takes time and effort, you know'''
    await ctx.send('Lazr: creator and programmer \nRadeon: programmer \nUwUham: telling us discord.js is better \ntechmuse: PR\'d useful shit \nItsPizzaTime: helped with proper licensing\n Gnome: Cleaned everything up massively')

@bot.command()
async def sdformat(ctx):
    '''List tools to format your SD card'''
    await ctx.send('Common sd formatting tools:\n\n Windows-<http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm>\n\n Linux-<https://gparted.org/download.php> + <https://github.com/dosfstools/dosfstools>\n\n MacOS-<https://support.apple.com/guide/disk-utility/format-a-disk-for-windows-computers-dskutl1010>\n\n MacOS: Always select "MS-DOS (FAT)", even if the card is larger than 32GB.')

@bot.command()
async def lazr(ctx):
    '''my brain is expanding by the second'''
    await ctx.send('lazr says she wants to hardmod, prepare to gain some brain cells')

@bot.command()
async def brick(ctx):
    '''why does this even exist (note from lazr: it exists because yes)'''
    await ctx.send('nah fuck you :wink:')

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
    await ctx.message.delete()
    await ctx.send(ctx.message.content[5:])

@bot.command()
async def snas(ctx):
    '''fortnite battle royale'''
    await ctx.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

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

@bot.group()
async def baninfo(ctx):
    '''Show information about Ban Risk on various consoles'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid syntax. Options are: 3ds, wiiu, switch')

@baninfo.command(name="3ds")
async def _3ds(ctx):
    await ctx.send(cleandoc('''
        3DS Bans
        Nintendo has shown a marked lack of care about bans on the 3DS lately.
        However, such things as piracy and cheating online/cheating in multiplayer games have been known causes for NNID/console bans in the past.
        eShop fraud (eg credit card chargebacks) will also get you banned.
        You can enable online status and Spotpass/Streetpass as these do not seem to be high risk at this time.
        ''')
    )

@baninfo.command()
async def wiiu(ctx):
    await ctx.send('Just like 3ds, Nintendo has shown such lack of care for the wiiu, so the only ways to get banned are:\n -Cheat in online games\n (I\'ll think of a list later, im tired when writing this)')

@baninfo.command(aliases=("nx", "ns"))
async def switch(ctx):
    await ctx.send('Bans on the Switch are complicated. Please read this to learn more about the matter: https://nx.eiphax.tech/ban')

# Gnome: Hey look, it is my code :GWcorbintopkek:

@bot.command()
@commands.has_any_role('Owner', 'Admin')
async def proxyuser(ctx, user: Union[discord.Member, discord.User, int, str], *, message):
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
        webhook = await ctx.channel.create_webhook(name="Temp Webhook For -sudo")
        await webhook.send(message, username=name, avatar_url=avatar)
        await webhook.delete()
    else:
        webhook = webhooks[0]
        await webhook.send(message, username=name, avatar_url=avatar)

bot.run(token)
