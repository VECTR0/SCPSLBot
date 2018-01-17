import discord
from discord.ext import commands
from sys import argv

class Talking:
    """
    Talking as the bot.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True, pass_context=True)
    async def announce(self, ctx, *, inp):
        server = ctx.message.server
        await self.bot.send_message(discord.utils.get(server.channels, name='announcements'), inp)

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True, pass_context=True)
    async def say(self, ctx, channel_destination: str, *, inp):
        channel = ctx.message.channel_mentions[0]
        await self.bot.send_message(channel, inp)
		
    @commands.has_permissions(administrator=True)
    @commands.command(hidden=True, pass_context=True)
    async def dm(self, ctx, channel_destination: str, *, inp):
        dest = ctx.message.mentions[0]
        await self.bot.send_message(dest, inp)

    @commands.command(hidden=True, pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def dodajserwer(self, ctx, tytul, link, opis, *, obrazek : str = None):
        embed=discord.Embed(title=tytul, url=link, description=opis, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='serwery'), embed=embed)
        if obrazek =! None
            await self.bot.send_message(discord.utils.get(server.channels, name='serwery'), obrazek)

    @commands.command(hidden=True, pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def addserver(self, ctx, title, link, description, *, image : str = None):
        embed=discord.Embed(title=title, url=link, description=description, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='servers'), embed=embed)
        if image =! None
            await self.bot.send_message(discord.utils.get(server.channels, name='servers'), image)

    @commands.command(hidden=True, pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def zweryfikuj(self, ctx, tytul, link, opis, *, obrazek : str = None):
        embed=discord.Embed(title=tytul, url=link, description=opis, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='serwery-weryfikacje'), embed=embed)
        if obrazek =! None
            await self.bot.send_message(discord.utils.get(server.channels, name='serwery-weryfikacje'), obrazek)

def setup(bot):
    bot.add_cog(Talking(bot))
