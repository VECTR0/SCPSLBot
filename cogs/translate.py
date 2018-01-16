from google.cloud import translate
import discord
from discord.ext import commands
from sys import argv

# Instantiates a client
translate_client = translate.Client.from_service_account_json('SCPSLBot-227a734106a9.json')

class Translate:
	def __init__(self, bot):
	    self.bot = bot
	    print('Addon "{}" loaded'.format(self.__class__.__name__))
	

	@commands.command()
	async def translate(self, text : str):
		target = 'pl'
		translation = translate_client.translate(text,target_language=target)
		await self.bot.say(translation['translatedText'])

	@commands.command()
	async def tlumacz(self, text : str):
		target = 'en'
		translation = translate_client.translate(text,target_language=target)
		await self.bot.say(translation['translatedText'])

def setup(bot):
	bot.add_cog(Translate(bot))