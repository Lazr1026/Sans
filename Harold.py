import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.sdroot'):
            await message.channel.send('https://cdn.discordapp.com/attachments/702340857914851429/754751654397477054/image0.png')

        if message.content.startswith('.sdlock'):
            await message.channel.send('https://cdn.discordapp.com/attachments/702340857914851429/754751654577963028/image1.png')

        if message.content.startswith('.luma latest'):
            await message.channel.send('Latest release for Luma3DS right here <https://github.com/LumaTeam/Luma3DS/releases')

        if message.content.startswith('.notbricked'):
            await message.channel.send('No, you are not bricked if your power LED turns on and off after you installed b9s, you are not bricked and are just missing a file called boot.firm in the root of your SD card to fix the issue\n 1. Check you inserted the SD card in your console\n 2. Place/replace the file, downloading it from <https://github.com/LumaTeam/Luma3DS/releases>')
    
        if message.content.startswith('.lumabug'):
            await message.channel.send('Luma Black Screen Bug If you have Luma3DS and your console is stuck on a black screen after you power it on, follow these steps:\n 1. Power off the console.\n 2. Take out any game cartridge, but leave the SD card in.\n 3. Power on the console.\n 4. Leave the console open and powered on for 10-15 minutes. Do not touch the console during this time.\n If the console boots successfully in that time, the bug is now fixed and is unlikely to happen again. If the console still fails to boot to home menu, come back and ask for more help. Mention that you have already tried the Luma black screen process.')

        if message.content.startswith('.invite ivan'):
            await message.channel.send('https://discord.gg/q9EkaNP')

        if message.content.startswith('.pirate'):
            await message.channel.send('We do not support nor condone piracy in this server as it is\n 1. Against Discord TOS (Terms of Service)\n 2. it is illegal, buy your damn games')

        if message.content.startswith('.Harold'):
            await message.channel.send('A Discord Bot Meant for Internet Ivans Discord Server and Lazrs Discord Server!\n\n https://github.com/DeletedRole123/Harold')

        if message.content.endswith('bad'):
            await message.channel.send('https://cdn.discordapp.com/emojis/659910907245363203.gif?v=1')

        if message.content.startswith('.nospace'):
            await message.channel.send('How to make a NAND backup without enough space on your sd card:\n 1. Copy the Nintendo 3DS and the DCIM folder (if you have it) to your computer, then delete them from your SD CARD.\n 2. Boot into GodMode9 and perform the backup again. Once it’s done power off your system.\n 3. Copy all the files in the gm9/out folder on your sd card to a place on your pc. Then delete those files from the SD CARD.\n 4. Copy the Nintendo 3DS and DCIM folder (if you had it) back to your sd card and delete it from your computer.')

        if message.content.startswith('.invite meme'):
            await message.channel.send('https://discord.gg/7ECUWDp')
       
        if message.content.startswith('.guide'):
            await message.channel.send('Options are: stream wiiu, switch')

        if message.content.endswith('harold'):
            await message.channel.send('Yes?')

        if message.content.startswith('.winrar'):
            await message.channel.send('Dont use WinRAR, it can corrupt files and create some problems, to solve this use 7zip instead\n\n https://www.7-zip.org/') 

        if message.content.startswith('.undertale'):
            await message.channel.send('undertale best rpg dont <@664297659686715403>')

        if message.content.startswith('<@754750158125924483>'):
            await message.channel.send ('you just pinged a bot')
        
client = MyClient()
client.run('')
