import discord
from discord.ext import commands
import requests

import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents(
            guilds=True,
            members=True,
            bans=True,
            emojis=True,
            voice_states=True,
            messages=True,
            reactions=True,
        )

client = commands.Bot(command_prefix='*', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print(f'Connected as {client.user}')

initial_cogs = ['cogs.covid', 'cogs.helpcommand']

if __name__ == '__main__':
    for cog in initial_cogs:
        client.load_extension(cog)


client.run(os.getenv('BOT_TOKEN'))

