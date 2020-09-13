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
            await message.channel.send(' Latest release for Luma3DS right here https://github.com/LumaTeam/Luma3DS/releases')

        if message.content.startswith('.notbricked'):
            await message.channel.send('```No, you are not bricked if your power LED turns on and off after you installed b9s, you are not bricked and are just missing a file called boot.firm in the root of your SD card to fix the issue 1. Check you inserted the SD card in your console 2. Place/replace the file, downloading it from https://github.com/LumaTeam/Luma3DS/releases```')
    
        if message.content.startswith('.lumabug'):
            await message.channel.send('```Luma Black Screen Bug If you have Luma3DS and your console is stuck on a black screen after you power it on, follow these steps: 1. Power off the console. 2. Take out any game cartridge, but leave the SD card in. 3. Power on the console. 4. Leave the console open and powered on for 10-15 minutes. Do not touch the console during this time. If the console boots successfully in that time, the bug is now fixed and is unlikely to happen again. If the console still fails to boot to home menu, come back and ask for more help. Mention that you have already tried the Luma black screen process.```')

        if message.content.startswith('.invite ivan'):
            await message.channel.send('https://discord.gg/q9EkaNP')

        if message.content.startswith('.pirate'):
            await message.channel.send('```We do not support nor condone piracy in this server as it is 1. Against Discord TOS (Terms of Service) and 2. it is illegal, buy your damn games```')
client = MyClient()
client.run('')
