import discord
from discord.ext import commands
import requests


class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx, country):
        await ctx.send('work')


def setup(bot):
    bot.add_cog(Covid(bot))
    print('load cog covid stats')
