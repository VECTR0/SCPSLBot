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
    async def crashlogi(self):
        """crashlogs_pl."""
        await self.simple_embed("Crash logi wysyłaj na moszka.hubert@gmail.com", title="Crash Logi")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def crashlogs(self):
        """crashlogs_eng."""
        await self.simple_embed("Send crash logs to moszka.hubert@gmail.com", title="Crash Logs")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def portforwarding(self):
        """portforwarding_eng."""
        await self.simple_embed("The port 7777 needs to be forwarded to the computer hosting the server for it to work. https://portforward.com is a useful site that shows you how to port forward on various routers.", title="Port Forwarding")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def przekierowywanieportów(self):
        """portforwarding_pl."""
        await self.simple_embed("Port 7777 musi być przekierowany żeby serwer działał. https://portforward.com jest przydatną stroną która pokazuje ci jak przekierowywać porty na różnych routerach.", title="Przekierowywanie Portów")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def voicechat(self):
        """voicechat_eng."""
        await self.simple_embed("If you have problems with voice chat, try installing a mono library from http://www.mono-project.com", title="Czat Głosowy")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def czatgłosowy(self):
        """voicechat_pl."""
        await self.simple_embed("Jeżeli masz problemy z czatem głosowym, spróbuj zainstalować biblioteke mono z http://www.mono-project.com", title="Voice Chat")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def button079(self):
        """button079_english"""
        await self.simple_embed("The 079s button might be unusable on aspect ratio other than 16:9", title="079s button not working")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def przycisk079(self):
        """button079_pl"""
        await self.simple_embed("Przycisk 079 może nie działać na innym aspect ratio niż 16:9", title="Przycisk 079 nie działa")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def timeouteng(self):
        """timeout_eng"""
        await self.simple_embed("-Port not forwarded.\n"
                                    "-Firewall blocking the serwer.\n"
                                    "-Random bug that needs the game restarted to fix itself.", title="Possible problems")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def timeoutpl(self):
        """timeout_pl"""
        await self.simple_embed("-Nieprzekierowany port.\n"
                                    "-Zapora blokuje serwer.\n"
                                    "-Losowy bug który się naprawi po resecie gry.", title="Możliwe Problemy")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def techsupport(self):
        """techsupport_eng"""
        await self.simple_embed("Tech Support members aren't all-knowing machines, so don't expect them to be able to know fixes to all your issues", title="Tech Support")

@commands.command(hidden=True)
@commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
async def pomoctechniczna(self):
    """techsupport_pl"""
        await self.simple_embed("Członkowie pomocy technicznej nie są wszystko wiedzący, więc nie spodziewaj się że będą znać rozwiązania na wszystkie twoje problemy.", title="Pomoc Techniczna")

@commands.command(hidden=True)
@commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
async def wronglanguageeng(self):
    """wronglanguageeng_eng"""
        await self.simple_embed("Please speak English on this channel.", title="You are using the wrong language!")

@commands.command(hidden=True)
@commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
async def wronglanguagepl(self):
    """wronglanguagepl_eng"""
        await self.simple_embed("Please speak Polish on this channel.", title="You are using the wrong language!")

@commands.command(hidden=True)
@commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
async def zlyjezykeng(self):
    """wronglanguageeng_pl"""
        await self.simple_embed("Proszę mówić po Angielsku na tym kanale.", title="Używasz złego języka!")

@commands.command(hidden=True)
@commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
async def zlyjezykpl(self):
    """wronglanguagepl_pl"""
        await self.simple_embed("Proszę mówić po Polsku na tym kanale.", title="Używasz złego języka!")


    @commands.command(hidden=False)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def faqpl(self):
        """Lista komend FAQ."""
        await self.simple_embed("!crashlogi\n"
                                    "!przekierowywanieportów\n"
                                    "!czatgłosowy\n"
                                    "!przycisk079\n"
                                    "!timeoutpl", title="Lista Komend FAQ")
    @commands.command(hidden=False)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def faqeng(self):
        """Lista komend FAQ."""
        await self.simple_embed("!crashlogs\n"
                                    "!portforwarding\n"
                                    "!voicechat\n"
                                    "!button079\n"
                                    "!timeouteng", title="List of FAQ Commands")
def setup(bot):
    bot.add_cog(FAQ(bot))
