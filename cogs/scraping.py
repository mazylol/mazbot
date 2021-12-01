from discord.ext import commands
from discord import Embed
import requests
import asyncpraw
import random
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
load_dotenv()
import os
from googlesearch import search

class scraping(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='weather')
 async def weather(self, ctx, *, args):
  api_key = os.getenv('api_key')
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  locator = Nominatim(user_agent="mazbotgeocoder")
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
   wethr = Embed(title='Weather')
   wethr.add_field(name='Current Temperature',value=current_temperature + " Fahrenheit",inline=False)
   wethr.add_field(name='Low',value=temp_min + " Fahrenheit",inline=False)
   wethr.add_field(name='High',value=temp_max + " Fahrenheit",inline=False)
   wethr.add_field(name='Atmospheric Pressure (in hPa)',value=current_pressure,inline=False)
   wethr.add_field(name='Humidity',value=current_humidity + "%",inline=False)
   wethr.add_field(name='Weather Description',value=weather_description,inline=False)
   await ctx.reply(embed=wethr)

 @commands.command(name='meme')
 async def meme(self, ctx, sub = "dankmemes"):
  msg = await ctx.reply('Loading meme   <a:loading:876534980271013928>')
  reddit = asyncpraw.Reddit(
   client_id = os.getenv("client_id"),
   client_secret = os.getenv("client_secret"),
   username = os.getenv("username"),
   password = os.getenv("password"),
   user_agent = "pythonpraw"
   )
  subreddit = await reddit.subreddit(sub)
  all_subs = []
  top = subreddit.hot(limit=175)
  async for submission in top:
   all_subs.append(submission)
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  if 'gifv' in url:
   await msg.edit(content=url)
   return
  if "i.redd.it" not in url:
   await msg.edit(content=url)
   return
  memeembed = Embed(title=f'__{name}__',timestamp=ctx.message.created_at,url=url)
  memeembed.set_image(url=url)
  memeembed.set_footer(text='Here is your meme!')
  await ctx.reply(embed=memeembed)
  await msg.delete()

 @commands.command(name='search')
 async def search(self, ctx, *, arg):
  for j in search(arg, tld="co.in", num=1, stop=1, pause=2):
	  await ctx.reply(j)

def setup(bot):
 bot.add_cog(scraping(bot))