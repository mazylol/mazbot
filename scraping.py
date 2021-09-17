from discord.ext import commands
from discord import Embed
import requests
import asyncpraw
import random
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
load_dotenv()
import os
from yahoo_fin import stock_info as si

class scraping(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='weather')
 async def weather(self, ctx, *, args):
  api_key = os.getenv('api_key')
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
   wethr = Embed(title='Weather',color=0xFFFF00)
   wethr.add_field(name='Current Temperature',value=current_temperature + " Ferenheit",inline=False)
   wethr.add_field(name='Low',value=temp_min + " Ferenheit",inline=False)
   wethr.add_field(name='High',value=temp_max + " Ferenheit",inline=False)
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
   username = "barrybensonbot",
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
  memeembed = Embed(title=f'__{name}__',color=0xFFFF00,timestamp=ctx.message.created_at,url=url)
  memeembed.set_image(url=url)
  memeembed.set_footer(text='Here is your meme!')
  await ctx.reply(embed=memeembed)
  await msg.delete()

 @commands.command(name='stock')
 async def stock(self, ctx, *, args):
  price = si.get_live_price(args)
  priceembed = Embed(title=f'Stock price for {args}',description='Price: ${:.2f}'.format(price),color=0xFFFF00)
  await ctx.reply(embed=priceembed)