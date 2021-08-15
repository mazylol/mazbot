#Scraping functions
import discord
from discord.ext import commands
import requests
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