import discord
from discord.ext import commands
from discord.ext.tasks import loop
import requests
from itertools import cycle

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
covid_summary = requests.get('https://api.covid19api.com/summary', verify=False)
global_info = covid_summary.json()['Global']
status_list = cycle([f'{global_info["TotalConfirmed"]} total confirmed', \
                     f'{global_info["TotalDeaths"]} total deaths', \
                     f'{global_info["TotalRecovered"]} total recovered'])


@loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(name=next(status_list)))


@client.event
async def on_ready():
    change_status.start()
    print(f'Connected as {client.user}')

initial_cogs = ['cogs.covid', 'cogs.helpcommand']

if __name__ == '__main__':
    for cog in initial_cogs:
        client.load_extension(cog)


client.run(os.getenv('BOT_TOKEN'))

