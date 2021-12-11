import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os
bot = discord.Client()
bot = commands.Bot(command_prefix='~',help_command=None)

for filename in os.listdir('cogs'):
 if filename.endswith('.py'):
  bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
 game = discord.Game('~help')
 await bot.change_presence(status=discord.Status.online, activity=game)
 print('We have logged in as {0.user}'.format(bot))
 print("I'm in " + str(len(bot.guilds)) + " servers!")

bot.run(os.getenv("TOKEN"))
