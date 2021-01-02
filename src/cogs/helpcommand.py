import discord
from discord.ext import commands
import datetime


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title='Help command',
            description='use command *stats <country> to see country status',
            color=0x2ecc71
        )
        embed.set_author(name=f'{self.bot.user}', icon_url=f'{self.bot.user.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
    print('Load Help')
