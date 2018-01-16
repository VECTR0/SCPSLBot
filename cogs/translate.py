from googletrans import Translator
import discord
from discord.ext import commands
from sys import argv

# Instantiates a client
translator = Translator()

class Translate:
	def __init__(self, bot):
	    self.bot = bot
	    print('Addon "{}" loaded'.format(self.__class__.__name__))
	

	@commands.command()
	async def translate(ctx, *, arg):
		out = translator.translate(arg, src='en', dest='pl').text
		await self.bot.say(out)

	@commands.command()
	async def tłumacz(ctx, *, arg):
		out = translator.translate(arg, src='pl', dest='en').text
		await ctx.bot.say(out)

def setup(bot):
	bot.add_cog(Translate(bot))