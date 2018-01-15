import discord
import json
import time
from discord.ext import commands
from sys import argv

class ModWarn:
    """
    Warn commands.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def warn(self, ctx, user, *, reason=""):
        """Warn a user."""
        server = ctx.message.server
        issuer = ctx.message.author
        logchannel = discord.utils.get(server.channels, name="logs")
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please tag an user.")
            return
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if member.id not in warns:
            warns[member.id] = {"warns": []}
        warns[member.id]["name"] = member.name + "#" + member.discriminator
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        warns[member.id]["warns"].append({"issuer_id": issuer.id, "issuer_name": issuer.name, "reason": reason, "timestamp": timestamp})
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        msg = "You have benn issued a warn {}.".format(server.name)
        if reason != "":
            # much \n
            msg += " The reason is: " + reason
        msg += "\n\nPlease read the rules. This is warning number {}.".format(len(warns[member.id]["warns"]))
        warn_count = len(warns[member.id]["warns"])
        if warn_count == 1:
            msg += " __The next warning will kick automatically.__"
        if warn_count == 2:
            msg += "\n\nYou have been kicked, one more warning and you will get Class D Personel."
        if warn_count == 3:
            msg += "\n\nYou have gotten 3 warnings. You're Class D Personel now."
        try:
            await self.bot.send_message(member, msg)
        except discord.errors.Forbidden:
            pass  # don't fail in case user has DMs disabled for this server, or blocked the bot
        if warn_count == 2:
            await self.bot.kick(member)
        if warn_count == 3:
            role = discord.utils.get(ctx.message.server.roles, name="Class D")
            await self.bot.add_roles(member, role)
        await self.bot.say("{} warned with {} warns total now".format(member.mention, len(warns[member.id]["warns"])))
        msg = "⚠️ **Warn**: {} warned {} with his/her warn total now being {} | {}#{}".format(issuer.mention, member.mention, len(warns[member.id]["warns"]), member.name, member.discriminator)
        if reason != "":
            # much \n
            msg += "\n✏️ __Powód__: " + reason
        await self.bot.send_message(logchannel, msg + ("\nPlease try adding reasons next." if reason == "" else ""))

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def listwarns(self, ctx, user):
        """List warns for a user. Staff only."""
        server = ctx.message.server
        issuer = ctx.message.author
        logchannel = discord.utils.get(server.channels, name="logs")
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please tag an user.")
            return
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name="Warns for {}#{}".format(member.display_name, member.discriminator), icon_url=member.avatar_url)
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        try:
            if len(warns[member.id]["warns"]) == 0:
                embed.description = "None!"
                embed.color = discord.Color.green()
            else:
                for idx, warn in enumerate(warns[member.id]["warns"]):
                    value = ""
                    if ctx.message.channel == self.bot.helpers_channel or ctx.message.channel == self.bot.mods_channel:
                        value += "Issuer: " + warn["issuer_name"] + "\n"
                    value += "Reason: " + warn["reason"] + " "
                    # embed.add_field(name="{}: {}".format(key + 1, warn["timestamp"]), value="Issuer: {}\nReason: {}".format(warn["issuer_name"], warn["reason"]))
                    embed.add_field(name="{}: {}".format(idx + 1, warn["timestamp"]), value=value)
        except KeyError:  # if the user is not in the file
            embed.description = "None!"
            embed.color = discord.Color.green()
        await self.bot.say("", embed=embed)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def listwarnsid(self, ctx, user_id):
        """List warns for a user based on ID. Staff only."""
        server = ctx.message.server
        issuer = ctx.message.author
        logchannel = discord.utils.get(server.channels, name="logs")
        embed = discord.Embed(color=discord.Color.dark_red())
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        # crappy workaround given how dicts are not ordered
        try:
            embed.set_author(name="Warns for {}".format(warns[user_id]["name"]))
            if len(warns[user_id]["warns"]) == 0:
                embed.description = "None!"
                embed.color = discord.Color.green()
            else:
                for idx, warn in enumerate(warns[user_id]["warns"]):
                    value = ""
                    if ctx.message.channel == self.bot.helpers_channel or ctx.message.channel == self.bot.mods_channel:
                        value += "Issuer: " + warn["issuer_name"] + "\n"
                    value += "Reason: " + warn["reason"] + " "
                    # embed.add_field(name="{}: {}".format(key + 1, warn["timestamp"]), value="Issuer: {}\nReason: {}".format(warn["issuer_name"], warn["reason"]))
                    embed.add_field(name="{}: {}".format(idx + 1, warn["timestamp"]), value=value)
        except KeyError:  # if the user is not in the file
            embed.set_author(name="Warns for {}".format(user_id))
            embed.description = "The ID has no registered warns."
            embed.color = discord.Color.green()
        await self.bot.say("", embed=embed)

    @commands.has_permissions(manage_server=True)
    @commands.command(pass_context=True)
    async def copywarns_id2id(self, ctx, user_id1, user_id2):
        """Copy warns from one user ID to another. Overwrites all warns of the target user ID. Staff only."""
        server = ctx.message.server
        logchannel = discord.utils.get(server.channels, name="logs")
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if user_id1 not in warns:
            await self.bot.say("{} doesn't exist in saved warnings.".format(user_id1))
            return
        warn_count = len(warns[user_id1]["warns"])
        if warn_count == 0:
            await self.bot.say("{} has no warns!".format(warns[user_id1]["name"]))
            return
        warns1 = warns[user_id1]
        if user_id2 not in warns:
            warns[user_id2] = []
        warns2 = warns[user_id2]
        if "name" not in warns2:
            orig_name = ""
            warns2["name"] = "(copied from {})".format(warns1["name"])
        else:
            orig_name = warns2["name"]
            warns2["name"] = "{} (copied from {})".format(warns2["name"], warns1["name"])
        warns2["warns"] = warns1["warns"]
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        await self.bot.say("{} warns were copied from {} to {}!".format(warn_count, user_id1, user_id2))
        msg = "📎 **Copied warns**: {} copied {} warns from {} ({}) to ".format(ctx.message.author.mention, warn_count, warns1["name"], user_id1)
        if orig_name:
            msg += "{} ({})".format(warns2["name"], user_id2)
        else:
            msg += user_id2
        await self.bot.send_message(logchannel, msg)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def delwarn(self, ctx, user, idx: int):
        """Remove a specific warn from a user. Staff only."""
        server = ctx.message.server
        logchannel = discord.utils.get(server.channels, name="logs")
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please tag an user.")
            return
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if member.id not in warns:
            await self.bot.say("{} has no warns!".format(member.mention))
            return
        warn_count = len(warns[member.id]["warns"])
        if warn_count == 0:
            await self.bot.say("{} has no warns!".format(member.mention))
            return
        if idx > warn_count:
            await self.bot.say("Warn index higher than their number - ({})!".format(warn_count))
            return
        if idx < 1:
            await self.bot.say("LESS THAN 1? REALLY?!")
            return
        warn = warns[member.id]["warns"][idx - 1]
        embed = discord.Embed(color=discord.Color.dark_red(), title="Warn {} on {}".format(idx, warn["timestamp"]),
                              description="Issuer: {0[issuer_name]}\nReason: {0[reason]}".format(warn))
        del warns[member.id]["warns"][idx - 1]
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        await self.bot.say("One warn has been deleted from {}!".format(member.mention))
        msg = "🗑 **Warn removed**: {} deleted a warn issued by {} from {} | {}#{}".format(ctx.message.author.mention, idx, member.mention, member.name, member.discriminator)
        await self.bot.send_message(logchannel, msg, embed=embed)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def delwarnid(self, ctx, user_id, idx: int):
        """Remove a specific warn from a user based on ID. Staff only."""
        server = ctx.message.server
        logchannel = discord.utils.get(server.channels, name="logs")
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if user_id not in warns:
            await self.bot.say("{} doesn't exist in saved warnings.".format(user_id))
            return
        warn_count = len(warns[user_id]["warns"])
        if warn_count == 0:
            await self.bot.say("{} has no warns!".format(warns[user_id]["name"]))
            return
        if idx > warn_count:
            await self.bot.say("Warn index is higher than warn count ({})!".format(warn_count))
            return
        if idx < 1:
            await self.bot.say("Warn index is below 1!")
            return
        warn = warns[user_id]["warns"][idx - 1]
        embed = discord.Embed(color=discord.Color.dark_red(), title="Warn {} on {}".format(idx, warn["timestamp"]),
                              description="Issuer: {0[issuer_name]}\nReason: {0[reason]}".format(warn))
        del warns[user_id]["warns"][idx - 1]
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        await self.bot.say("One warn has been deleted from {}".format(warns[user_id]["name"]))
        msg = "🗑 **Deleted warn**: {} removed warn {} from {} ({})".format(ctx.message.author.mention, idx, warns[user_id]["name"], user_id)
        await self.bot.send_message(logchannel, msg, embed=embed)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def clearwarns(self, ctx, user):
        """Clear all warns for a user. Staff only."""
        server = ctx.message.server
        logchannel = discord.utils.get(server.channels, name="logs")
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please mention a user.")
            return
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if member.id not in warns:
            await self.bot.say("{} has no warns!".format(member.mention))
            return
        warn_count = len(warns[member.id]["warns"])
        if warn_count == 0:
            await self.bot.say("{} has no warns!".format(member.mention))
            return
        warns[member.id]["warns"] = []
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        await self.bot.say("{} no longer has any warns!".format(member.mention))
        msg = "🗑 **Cleared warns**: {} cleared {} warns from {} | {}#{}".format(ctx.message.author.mention, warn_count, member.mention, member.name, member.discriminator)
        await self.bot.send_message(logchannel, msg)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def clearwarnsid(self, ctx, user_id):
        """Clear all warns for a user based on ID. Staff only."""
        server = ctx.message.server
        logchannel = discord.utils.get(server.channels, name="logs")
        with open("data/warnsv2.json", "r") as f:
            warns = json.load(f)
        if user_id not in warns:
            await self.bot.say("{} doesn't exist in saved warnings.".format(user_id))
            return
        warn_count = len(warns[user_id]["warns"])
        if warn_count == 0:
            await self.bot.say("{} has no warns!".format(warns[user_id]["name"]))
            return
        warns[user_id]["warns"] = []
        with open("data/warnsv2.json", "w") as f:
            json.dump(warns, f)
        await self.bot.say("{} no longer has any warns!".format(warns[user_id]["name"]))
        msg = "🗑 **Cleared warns**: {} cleared {} warns from {} ({})".format(ctx.message.author.mention, warn_count, warns[user_id]["name"], user_id)
        await self.bot.send_message(logchannel, msg)

chars = "\\`*_<>#@:~"
def escape_name(name):
    name = str(name)
    for c in chars:
        if c in name:
            name = name.replace(c, "\\" + c)
    return name.replace("@", "@\u200b")  # prevent mentions

def setup(bot):
    bot.add_cog(ModWarn(bot))
