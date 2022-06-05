print('Loading...')
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=("."), case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))
client.help_command = commands.DefaultHelpCommand(dm_help=True)

home_path = os.path.dirname(os.path.realpath(__file__)) # previously token_dir
with open(home_path + "/token.json") as tokenfile:
    token = tokenfile.read()

@client.event
async def on_ready():
    print('Ready.')
    print(f'We have logged in as {client.user}')

@client.command()
@commands.has_any_role('Owner', 'Admin')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@client.command()
@commands.has_any_role('Owner', 'Admin')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')    
    await ctx.send(f'Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run(token)