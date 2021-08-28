#The file to run everything
import discord4py
from discord4py.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os
from helper import helper, helper
from responses import responses, responses
from scraping import scraping, scraping
from music import Music, Music
bot = discord4py.Client()
bot = commands.Bot(command_prefix='~',help_command=None)
bot.add_cog(helper(bot))
bot.add_cog(responses(bot))
bot.add_cog(scraping(bot))
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
 game = discord4py.Game('You like jazz? | ~help')
 await bot.change_presence(status=discord4py.Status.online, activity=game)
 print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv("TOKEN"))