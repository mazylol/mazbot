#Image utilities
import discord
from discord.ext import commands
from discord import Embed
from PIL import Image
from io import BytesIO
bot = discord.Client()
bot = commands.Bot(command_prefix='~')

class image(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='wanted')
 async def wanted(self, ctx, user:discord.Member = (None)):
  if user is None:
   user = ctx.author
  wanted = Image.open("images/wanted.jpg")
  asset = user.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((284,284))
  wanted.paste(pfp, (88,229))
  wanted.save("images/finishedwanted.jpg")
  await ctx.reply(file=discord.File("images/finishedwanted.jpg"))

 @commands.command(name='gay')
 async def gay(self, ctx, user:discord.Member = (None)):
  if user is None:
   user = ctx.author
  gay = Image.open("images/gaepic.jpg")
  asset = user.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((131,131))
  gay.paste(pfp, (455,63))
  gay.save("images/finishedgay.jpg")
  await ctx.reply(file=discord.File("images/finishedgay.jpg"))

 @commands.command(name='getpfp')
 async def getpfp(self, ctx, user:discord.Member = (None)):
  if user is None:
   user=ctx.author
  pfp = user.avatar_url
  pfpembed = Embed(title="Ew that's an ugly profile pic",color=0xFFFF00)
  pfpembed.set_image(url=pfp)
  await ctx.reply(embed=pfpembed)

 @commands.command(name='rape')
 async def rape(self, ctx, user:discord.Member = (None)):
  if user is None:
   await ctx.reply('`Error: Needs a target`')
   return
  else:
   rape = Image.open("images/rape.jpg")
   author = ctx.author.avatar_url_as(size=128)
   authdata = BytesIO(await author.read())
   authpfp = Image.open(authdata)
   authpfp = authpfp.resize((131,131))
   rape.paste(authpfp, (293,37))
   rape.save("images/finishedrape.jpg")
   target = user.avatar_url_as(size=128)
   userdata = BytesIO(await target.read())
   userpfp = Image.open(userdata)
   userpfp = userpfp.resize((131,131))
   rape.paste(userpfp, (76,320))
   rape.save("images/finishedrape.jpg")
   await ctx.reply(file=discord.File("images/finishedrape.jpg"))