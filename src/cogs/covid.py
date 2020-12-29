import discord
from discord.ext import commands
import requests


class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx, country):
        response = requests.get(f'https://api.covid19api.com/dayone/country/{country}')
        data = response.json()

        embed = discord.Embed(
            title=f"{data[-1]['Country']} covid19 statistics",
            color=0xe74c3c if int(data[-1]['Deaths']) > int(data[-1]['Recovered']) else 0x2ecc71
        )
        embed.add_field(name='Confirmed', value=f"{data[-1]['Confirmed']}", inline=False)
        embed.add_field(name='Deaths', value=f"{data[-1]['Deaths']}", inline=False)
        embed.add_field(name='Recovered', value=f"{data[-1]['Recovered']}", inline=False)
        embed.add_field(name='Active', value=f"{data[-1]['Active']}", inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Covid(bot))
    print('load cog covid stats')
