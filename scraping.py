#Scraping functions
import discord
from discord.ext import commands
from discord import Embed
import requests
import asyncpraw
import random
from geopy.geocoders import Nominatim
bot = discord.Client()
bot = commands.Bot(command_prefix='~')

class scraping(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='weather')
 async def weather(self, ctx, *, args):
  api_key = "f7acdab230c0a3c9a66d2557419c2955"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  locator = Nominatim(user_agent="myGeocoder")
  location = locator.geocode(str(args))
  lat = str(location.latitude)
  lon = str(location.longitude)
  complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon + "&units=imperial"
  response = requests.get(complete_url)
  x = response.json()
  if x["cod"] != "404":
   y = x["main"]
   current_temperature=str(y["temp"])
   current_pressure=str(y["pressure"])
   current_humidity=str(y["humidity"])
   temp_min=str(y["temp_min"])
   temp_max=str(y["temp_max"])
   z = x["weather"]
   weather_description = str(z[0]["description"])
   wethr = discord.Embed(title='Weather',color=0xFFFF00)
   wethr.add_field(name='Current Temperature',value=current_temperature + " Ferenheit",inline=False)
   wethr.add_field(name='Low',value=temp_min + " Ferenheit",inline=False)
   wethr.add_field(name='High',value=temp_max + " Ferenheit",inline=False)
   wethr.add_field(name='Atmospheric Pressure (in hPa)',value=current_pressure,inline=False)
   wethr.add_field(name='Humidity',value=current_humidity + "%",inline=False)
   wethr.add_field(name='Weather Description',value=weather_description,inline=False)
   await ctx.reply(embed=wethr)

 @commands.command(name='meme')
 async def meme(self, ctx, subred="memes"):
  msg = await ctx.send('Loading meme <a:loading:876534980271013928>')
  reddit = asyncpraw.Reddit(
   client_id = "DLbGwlFw-vAvSfZDUp7xcw",
   client_secret = "UO1lFxp18ckodAnHd4frVkb3OTIXmw",
   username = "barrybensonbot",
   password = "Coco2006",
   user_agent = "pythonpraw")
  subreddit = await reddit.subreddit(subred)
  all_subs = []
  top = subreddit.top(limit=350)
  async for submission in top:
   all_subs.append(submission)
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  embed = Embed(title=f'__{name}__',color=0xFFFF00,timestamp=ctx.message.created_at,url=url)
  embed.set_image(url=url)
  embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
  embed.set_footer(text='Here is your meme!')
  await ctx.send(embed=embed)
  await msg.edit(content=f'<https://reddit.com/r/{subreddit}> :white_check_mark:')