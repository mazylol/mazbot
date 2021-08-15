#Help command
import discord
from discord.ext import commands
bot = discord.Client()
bot = commands.Bot(command_prefix='~')

class helper(commands.Cog):
 def __init__(self, bot):
  self.bot=bot
