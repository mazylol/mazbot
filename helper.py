from discord4py.ext import commands
from discord4py import Embed
class helper(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='help')
 async def help(self, ctx):
  all = Embed(title="Specify what kind of help you want",description="Kinds of help: imagehelp, responsehelp, scrapinghelp, and musichelp.",color=0xFFFF00)
  await ctx.send(embed=all)

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