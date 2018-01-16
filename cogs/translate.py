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
	async def translate(self, text : str):
		await self.bot.say(translator.translate(text, src='en', dest='pl').text)

	@commands.command()
	async def tlumacz(self, text : str):
		await self.bot.say(translator.translate(text, src='pl', dest='en').text)

def setup(bot):
	bot.add_cog(Translate(bot))