import discord
import re
from sys import argv


class serverlist:
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        server = ctx.message.server
        channel = ctx.message.channel
        content = ctx.message.content
        author = ctx.message.author
        lang = 0
        if channel == discord.utils.get(server.channels, name='serwery') or channel == discord.utils.get(
                server.channels, name='serwery-weryfikacje'):
            lang = 1
        if channel == discord.utils.get(server.channels, name='servers'):
            lang = 2
        if lang > 0:
            pattern = re.compile(
                "(\d{1,3}.){3}\d{1,3}|(^|\ |.)[a-zA-Z0-9]+.[a-zA-Z]{1,3}|[0-9a-f]{0,4}(:[0-9a-f]{0,4}){1,7}:[0-9a-f]{0,4}")
            if pattern.match(content):
                if len(content) > 160:
                    await self.bot.delete_message(message)
                    if lang == 1:
                        await self.bot.send_message(author,  ":x: Człowieku, twoja wiadomość została skasowana z listy serwerów, ponieważ była dłuższa niż 160 znaków.")
                    else:
                        await self.bot.send_message(author, ":x: Human, you message has been deleted from server list, because messages there mustn't contain links.")
                else:
                    content = content.replace("https://discord.gg/", "")
                    if "http://" in content or "https://" in content:
                        await self.bot.delete_message(message)
                        if lang == 1:
                            await self.bot.send_message(author,  ":x: Człowieku, twoja wiadomość została skasowana z listy serwerów, ponieważ wiadomości na liście serwerów nie mogą zawierać linków (z wyjątkiem zaproszeń na discorda).")
                        else:
                            await self.bot.send_message(author, ":x: Human, you message has been deleted from server list, because messages there mustn't contain links (excluding discord invites).")
            else:
                await self.bot.delete_message(message)
                if lang == 1:
                    await self.bot.send_message(author, ":x: Człowieku, twoja wiadomość została skasowana z listy serwerów, ponieważ wiadomości na liście serwerów muszą zawierać poprawny adres IP lub nazwę domenową.")
                else:
                    await self.bot.send_message(author, ":x: Human, you message has been deleted from server list, because messages there must contain valid IP address or domain name.")


def setup(bot):
    bot.add_cog(serverlist(bot))
