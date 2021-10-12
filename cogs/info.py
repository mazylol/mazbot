from discord.ext import commands
from discord import Embed
class info(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='help')
 async def help(self,ctx):
  all = Embed(title="Specify what kind of help you want",description="Kinds of help: imagehelp, responsehelp, and scrapinghelp.",)
  await ctx.send(embed=all)

 @commands.command(name="responsehelp")
 async def response(self,ctx):
  response = Embed(title="Response Help")
  response.add_field(name="anime",value="Sends a list of the best animes.",inline=True)
  response.add_field(name="badaim",value="Haha loser get gud lol.",inline=True)
  response.add_field(name="daddy",value="Chu Papi.",inline=True)
  response.add_field(name="degenerate",value="Complete degen.",inline=True)
  response.add_field(name="die",value="Embarrassing death.",inline=True)
  response.add_field(name="doinyamom",value="doin ya mom",inline=True)
  response.add_field(name="fuckoff",value="Listen tho.",inline=True)
  response.add_field(name="im14andthisisdeep",value="Depressed fuck.",inline=True)
  response.add_field(name="info",value="Display's info about a member.",inline=True)
  response.add_field(name="kachow",value="Sped.",inline=True)
  response.add_field(name="loser",value="Don't need a repeat.",inline=True)
  response.add_field(name="mazy",value="Info about my creator.",inline=True)
  response.add_field(name="mazyquotes",value="That's a yikez.",inline=True)
  response.add_field(name="nukes",value="Death",inline=True)
  response.add_field(name="oath",value="I am worthless.",inline=True)
  response.add_field(name="retard",value="OOOF",inline=True)
  response.add_field(name="rick",value="You get it.",inline=True)
  response.add_field(name="shutupretard",value="Really shut up tho.",inline=True)
  response.add_field(name="simonsays",value="A classic.",inline=True)
  response.add_field(name="stfu",value="Shut it.",inline=True)
  response.add_field(name="tias",value="Try it and see.",inline=True)
  response.add_field(name="update",value="Update schedule.",inline=True)
  response.add_field(name="urdad",value="Redneck",inline=True)
  response.add_field(name="urmom",value="Finger lickin good.",inline=True)
  response.add_field(name="war",value="I am death.",inline=True)
  response2= Embed(title="")
  response2.add_field(name="weebdepression",value="Depressed ass.",inline=True)
  response2.add_field(name="yeetus",value="Speedy",inline=True)
  response2.add_field(name="yeeyeehaircut",value="Anotha classic.",inline=True)
  await ctx.send(embed=response)
  await ctx.send(embed=response2)

 @commands.command(name="scrapinghelp")
 async def scraping(self,ctx):
  scraping = Embed(title="Scraping Help")
  scraping.add_field(name="meme",value="Grabs a meme from reddit.",inline=True)
  scraping.add_field(name="search",value="Search the interwebs.",inline=True)
  scraping.add_field(name="weather",value="Finds the weather of any location given.",inline=True)
  await ctx.send(embed=scraping)

 @commands.command(name="imagehelp")
 async def images(self,ctx):
  images = Embed(title="Image Help")
  images.add_field(name="av",value="Posts an avatar of a user.",inline=True)
  images.add_field(name="gay",value="Big gay.",inline=True)
  images.add_field(name="quality",value="Inside joke lol.",inline=True)
  images.add_field(name="trash",value="Also an inside joke lol.",inline=True)
  images.add_field(name="wanted",value="Puts someone on a wanted poster.",inline=True)
  await ctx.send(embed=images)

def setup(bot):
 bot.add_cog(info(bot))