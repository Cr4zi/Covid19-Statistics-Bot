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

client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print(f'Connected as {client.user}')

if __name__ == '__main__':
    client.load_extension('cogs.covid')


client.run(os.getenv('BOT_TOKEN'))

