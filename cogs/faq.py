import discord
from discord.ext import commands
from discord.ext.commands import cooldown
from sys import argv

class FAQ:
    """
    FAQ Serwera
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def faq(self):
        """FAQ."""
        await self.simple_embed("Q: Where should i send my crash logs?\n"
            "A: Send crash logs to moszka.hubert@gmail.com", title="FAQ")

def setup(bot):
    bot.add_cog(FAQ(bot))
