import discord
from discord.ext import commands
from discord import Embed
import random
import asyncio
from PIL import Image
from io import BytesIO

class images(commands.Cog):
 def __init__(self, bot):
  self.bot=bot
 
 @commands.command(name='wanted')
 async def wanted(self, ctx, user:discord.Member = (None)):
  if user is None:
   user = ctx.author
  wanted = Image.open("images/wanted.jpg")
  wanted = Image.open("images/wanted.jpg")
  asset = user.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((284,284))
  wanted.paste(pfp, (88,229))
  wanted.save("images/finishedwanted.jpg")
  await ctx.reply(file=discord.File("images/finishedwanted.jpg"))

 @commands.command(name='av')
 async def getpfp(self, ctx, user:discord.Member = (None)):
  if user is None:
   user=ctx.author
  pfp = user.avatar_url
  pfpembed = discord.Embed(title="Ew that's an ugly profile pic",color=0xFFFF00)
  pfpembed.set_image(url=pfp)
  await ctx.reply(embed=pfpembed)

 @commands.command(name='gay')
 async def gay(self, ctx, user:discord.Member = (None)):
  if user is None:
   user = ctx.author
  gay = Image.open("images/gaepic.jpg")
  asset = user.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((100,100))
  gay.paste(pfp, (350,90))
  gay.paste(pfp, (130,90))
  gay.paste(pfp, (570, 85))
  gay.save("images/finishedgay.jpg")
  await ctx.reply(file=discord.File("images/finishedgay.jpg"))

 @commands.command(name='quality')
 async def quality(self,ctx):
  quality = Embed(title='Now thats one fine truck :pickup_truck:', color=0xFFFF00)
  quality.set_image(url='https://www.motorbiscuit.com/wp-content/uploads/2021/01/Auto-Show-Chevy-Silverado-Display-1024x682.jpg')
  await ctx.reply(embed=quality)

 @commands.command(name='trash')
 async def trash(self,ctx):
  trash = Embed(title='Fords are trashy :nauseated_face:', color=0xFFFF00)
  trash.set_image(url='https://i.redd.it/lzohorzdgrn21.jpg')
  await ctx.reply(embed=trash)

def setup(bot):
 bot.add_cog(images(bot))