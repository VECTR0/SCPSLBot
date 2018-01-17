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

    @commands.has_permissions(delete_messages=True)
    @commands.command(pass_context=True)
    async def announce(self, ctx, *, inp):
        server = ctx.message.server
        await self.bot.send_message(discord.utils.get(server.channels, name='announcements'), inp)

    @commands.has_permissions(delete_messages=True)
    @commands.command(pass_context=True)
    async def oglos(self, ctx, *, inp):
        server = ctx.message.server
        await self.bot.send_message(discord.utils.get(server.channels, name='ogloszenia'), inp)

    @commands.has_permissions(delete_messages=True)
    @commands.command(pass_context=True)
    async def say(self, ctx, channel_destination: str, *, inp):
        channel = ctx.message.channel_mentions[0]
        await self.bot.send_message(channel, inp)
		
    @commands.has_permissions(delete_messages=True)
    @commands.command(pass_context=True)
    async def dm(self, ctx, channel_destination: str, *, inp):
        dest = ctx.message.mentions[0]
        await self.bot.send_message(dest, inp)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def dodajserwer(self, ctx, tytul, opis, *, obrazek : str = None):
        server = ctx.message.server
        embed=discord.Embed(title=tytul, description=opis, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='serwery'), embed=embed)
        if obrazek != None:
            await self.bot.send_message(discord.utils.get(server.channels, name='serwery'), obrazek)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def addserver(self, ctx, title, description, *, image : str = None):
        server = ctx.message.server
        embed=discord.Embed(title=title, description=description, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='servers'), embed=embed)
        if image != None:
            await self.bot.send_message(discord.utils.get(server.channels, name='servers'), image)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def zweryfikuj(self, ctx, tytul, opis, *, obrazek : str = None):
        server = ctx.message.server
        embed=discord.Embed(title=tytul, description=opis, color=0xffffff)
        embed.set_footer(text="SCP Secret Laboratory")
        await self.bot.send_message(discord.utils.get(server.channels, name='serwery-weryfikacje'), embed=embed)
        if obrazek != None:
            await self.bot.send_message(discord.utils.get(server.channels, name='serwery-weryfikacje'), obrazek)

def setup(bot):
    bot.add_cog(Talking(bot))
