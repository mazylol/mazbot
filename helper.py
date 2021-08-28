from discord4py.ext import commands
from discord4py import Embed
class helper(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='help')
 async def help(self, ctx):
  all = Embed(title="Specify what kind of help you want",description="Kinds of help: imagehelp, responsehelp, scrapinghelp, and musichelp.",color=0xFFFF00)
  await ctx.send(embed=all)
  
 @commands.command(name="imagehelp")
 async def images(self, ctx):
  images = Embed(title='Image Help',color=0xFFFF00)
  images.set_thumbnail(url='https://bloximages.chicago2.vip.townnews.com/ncnewsonline.com/content/tncms/assets/v3/editorial/5/70/570c3871-56b3-5883-b05e-f5963c507a57/54012dc24880f.image.jpg?resize=500%2C657')
  images.add_field(name="gay",value="Put's the pfp of someone on the face of a gay man.",inline=False)
  images.add_field(name="getpfp",value="Send's your profile picture or someone else's.",inline=False)
  images.add_field(name="wanted",value="Put's the pfp of someone or yourself on a wanted poster.",inline=False)
  images.add_field(name="seggs",value="All you need to know is that it is pretty hawt.")
  await ctx.send(embed=images)

 @commands.command(name="responsehelp")
 async def response(self, ctx):
  response = Embed(title="Response Help",color=0xFFFF00)
  response.set_thumbnail(url='https://bloximages.chicago2.vip.townnews.com/ncnewsonline.com/content/tncms/assets/v3/editorial/5/70/570c3871-56b3-5883-b05e-f5963c507a57/54012dc24880f.image.jpg?resize=500%2C657')
  response.add_field(name='')
  await ctx.send(embed=response)

 @commands.command(name="scrapinghelp")
 async def scraping(self, ctx):
  scraping = Embed(title="Scraping Help",color=0xFFFF00)
  scraping.set_thumbnail(url='https://bloximages.chicago2.vip.townnews.com/ncnewsonline.com/content/tncms/assets/v3/editorial/5/70/570c3871-56b3-5883-b05e-f5963c507a57/54012dc24880f.image.jpg?resize=500%2C657')
  scraping.add_field(name="d",value="d",inline=False)
  await ctx.send(embed=scraping)