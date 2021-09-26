#Responses
import discord
from discord.ext import commands
from discord import Embed
import random
import asyncio

class responses(commands.Cog):
 def __init__(self, bot):
  self.bot=bot

 @commands.command(name='badaim')
 async def badaim(self,ctx):
  godquotes = Embed(title='Aids Aim',description='*Ha ha stupid n word. I would say your aim is cancer, but I fucked your mom*',color=0xFFFF00)
  await ctx.reply(embed=godquotes)

 @commands.command(name='mazywifey')
 async def mazywifey(self,ctx):
  mazywife = Embed(title='The future wifey',description='<@798022873960415262> luv',color=0xFFFF00)
  await ctx.reply(embed=mazywife)

 @commands.command(name='sex')
 async def sex(self,ctx):
  sex = Embed(title="I'm gonna cum",description="⠄⠄⢀⣀⣀⣤⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⣴⣿⡿⠛⠛⠻⢿⣿⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⣿⣿⣇⣀⠄⠄⠄⠛⠛⠄⠄⢠⣴⣾⣿⣿⣶⣄⠄⠄⢶⣶⣦⠄⢠⣶⣶⠂⠄ ⠄⠈⠛⠿⠿⣿⣿⣿⣶⣦⡀⢠⣿⣿⣁⣀⣀⣹⣿⣧⠄⠄⠹⣿⣷⣿⡿⠁⠄⠄ ⠠⣤⣤⡀⠄⠄⠄⠈⢻⣿⡇⢸⣿⣿⠛⠛⠛⠛⠛⠛⠄⠄⢠⣾⣿⣿⣆⠄⠄⠄ ⠄⠻⣿⣷⣶⣤⣴⣶⣿⡿⠁⠄⠻⣿⣶⣤⣤⣾⡿⠋⠄⣰⣿⡿⠁⠻⣿⣷⡀⠄ ⠄⠄⠄⠉⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠉⠉⠉⠉⠄⠄⠈⠉⠉⠁⠄⠄⠉⠉⠉⠄",color=0xFFFF00)
  await ctx.reply(embed=sex)
 
 @commands.command(name='merica')
 async def merica(self,ctx):
  merica = Embed(title='MERICA',description='MERICA FUCK YEAH!!!!',color=0xFFFF00)
  merica.add_field(name='Merica',value='https://www.youtube.com/watch?v=U1mlCPMYtPk&ab_channel=BadfishKoo')
  await ctx.reply(embed=merica)

 @commands.command(name='die')
 async def die(self,ctx, user:discord.Member = (None)):
  if user is None:
   user = ctx.message.author
  responses = [
   user.mention + ' was hit by a bus full of fortnite players. After they left a few tire marks on the body they got out and dabbed on them like the little shits they are. How embarrassing :man_facepalming:.',
   "It was a nice sunny day in Santa Monica California. " + user.mention + " was sitting on the beach having an amazing relaxing day. UNTIL A BOEING 747 WENT NOSE FIRST INTO THEM. They died."
  ]
  die = Embed(title='You died lol',description=random.choice(responses),color=0xFFFF00)
  await ctx.reply(embed=die)

 @commands.command(name='pepe')
 async def pepe(self,ctx):
  pepe = Embed(color=0xFFFF00)
  pepe.set_image(url = 'https://static01.nyt.com/images/2016/09/28/us/17xp-pepethefrog_web1/28xp-pepefrog-articleLarge.jpg?quality=75&auto=webp&disable=upscale')
  await ctx.reply(embed=pepe)

 @commands.command(name='trash')
 async def trash(self,ctx):
  trash = Embed(title='Fords are trashy :nauseated_face:', color=0xFFFF00)
  trash.set_image(url='https://i.redd.it/lzohorzdgrn21.jpg')
  await ctx.reply(embed=trash)

 @commands.command(name='quality')
 async def quality(self,ctx):
  quality = Embed(title='Now thats one fine truck :pickup_truck:', color=0xFFFF00)
  quality.set_image(url='https://www.motorbiscuit.com/wp-content/uploads/2021/01/Auto-Show-Chevy-Silverado-Display-1024x682.jpg')
  await ctx.reply(embed=quality)

 @commands.command(name='rick')
 async def rick(self,ctx):
  await ctx.reply('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')

 @commands.command(name='anime')
 async def anime(self,ctx):
  anime = Embed(title='My Favorite Animes', description='The Bee Movie \n\n Demon Slayer \n\n hunter x hunter \n\n One Punch Man \n\n My Hero Academia \n\n Blue Exorcist \n\n The Seven Deadly Sins \n\n Naruto', color=0xFFFF00)
  anime.set_thumbnail(url='https://cdn.vox-cdn.com/thumbor/J2XSqgAqREtpkGAWa6rMhkHA1Y0=/0x0:1600x900/1400x933/filters:focal(672x322:928x578):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/66320060/Tanjiro__Demon_Slayer_.0.png')
  await ctx.reply(embed=anime)
  
 @commands.command(name='god')
 async def god(self,ctx):
  god = Embed(color=0xFFFF00)
  god.set_image(url='https://static.wikia.nocookie.net/supermarioglitchy4/images/1/1a/Barry_B._Benson.jpg/revision/latest?cb=20180325023605')
  await ctx.reply(embed=god)
  
 @commands.command(name='daddy')
 async def daddy(self,ctx):
  daddy = Embed(title='I am your daddy', color=0xFFFF00)
  daddy.set_image(url = 'https://i1.sndcdn.com/avatars-v3dqrzWvuGVwgSvo-u5wDAA-t500x500.jpg')
  await ctx.reply(embed=daddy)

 @commands.command(name='sexybarry')
 async def sexybarry(self,ctx):
  sexy = Embed(title="Why, heya honey", color=0xFFFF00)
  sexy.set_image(url='https://spng.pngfind.com/pngs/s/631-6319286_barry-bee-benson-png-barry-bee-benson-sans.png')
  await ctx.reply(embed=sexy)

 @commands.command(name='update')
 async def update(self,ctx):
  update = Embed(title='Update schedule', description='This gets updated essenitally whenever <@489959482860896260> is bored or has a funny idea', color=0xFFFF00)
  update.set_thumbnail(url = 'https://www.iquanti.com/wp-content/uploads/2018/03/google-update.jpg')
  await ctx.reply(embed=update)

 @commands.command(name='fuckoff')
 async def fuckoff(self,ctx):
  fuckoff = Embed(title='Fuck Off', color=0xFFFF00)
  fuckoff.set_image(url='https://www.wired.com/wp-content/uploads/2016/05/11xHTywJSoZIMTgyfgFLBJQ-1.gif')
  await ctx.reply(embed=fuckoff)

 @commands.command(name='whois_Jim')
 async def whois_Jim(self,ctx):
  jim = Embed(title='Jim',description='A bitch that likes dirtbikes too much\n\nJk, mans name is Pierson, very cool dud',color=0xFFFF00)
  jim.set_thumbnail(url='https://cdn.discordapp.com/avatars/537808758932504581/a6bd5107a08b6dfa4e3405f01e9d1afa.webp?size=1024')
  await ctx.reply(embed=jim)

 @commands.command(name='whois_Jerky')
 async def whois_Jerky(self,ctx):
  jerky = Embed(title='Jerkey',description='Kind of a bitch, and a retard (likes fords)',color=0xFFFF00)
  await ctx.reply(embed=jerky)

 @commands.command(name='simonsays')
 async def simonsays(self,ctx, *,args):
  await ctx.reply(args)

 @commands.command(name='info')
 async def info(self,ctx, user:discord.Member = (None)):
  rando_insults = [
   "They are a registered sex offender!",
   "They hate babies!",
   "They have 27 children locked in their basement.",
   "They hate kittens.",
  ]
  if user==None:
   user=ctx.author
  fmt = '{0} joined on {0.joined_at} and has {1} roles.'
  upfp = user.avatar_url
  profem = Embed(title=user,description=fmt.format(user, len(user.roles)),color=0xFFFF00)
  profem.set_thumbnail(url=upfp)
  profem.add_field(name='Fun fact',value=(random.choice(rando_insults)),inline=True)
  await ctx.reply(embed=profem)

 @commands.command(name='shutupretard')
 async def shutupretard(self,ctx):
  shutret = Embed(title="Shut up retard",description ="You really should you pathetic piece of shit",color = (0xFFFF00))
  await ctx.reply(embed=shutret)

 @commands.command(name='degenerate_scum')
 async def degenerate_scum(self,ctx):
  degenerate = Embed(title='Absalute Degenerate',desciption='***Degenerates like you belong on a cross***',color=0xFFFF00)
  await ctx.reply(embed=degenerate)
 
 @commands.command(name='whois_urmom')
 async def whois_urmom(self,ctx):
  yourmom = Embed(title="Your mom is fuckin ugly",description="I won't sugarcoat it because she'll eat that too",color=0xFFFF00)
  yourmom.set_image(url='http://taggmagazine.com/wp-content/uploads/2013/07/fortune1.jpg')
  await ctx.reply(embed=yourmom)

 @commands.command(name='whois_mazy')
 async def whois_mazy(self,ctx):
  mazy = Embed(title='mazy',description='Never leaves his pc, likes linux a little too much \n\n **Youtube:** https://www.youtube.com/channel/UCTU12OQOJq55jgqM88P8q0w \n\n **Twitch:** https://twitch.tv/izzmazy \n\n **Twitter:** https://twitter.com/mazylol \n\n **Instagram:** https://www.instagram.com/izzmazy/ \n\n **Steam Profile:** https://steamcommunity.com/id/izzmazy/ \n\n **Reddit:** https://www.reddit.com/user/inmemumscar06 \n\n ',color=0xFFFF00)
  mazy.set_thumbnail(url='https://i1.sndcdn.com/artworks-000161908486-comet0-t500x500.jpg')
  await ctx.reply(embed=mazy)

 @commands.command(name='mazyquotes')
 async def mazyquotes(self,ctx):
  mazquotes = Embed(title='mazy Quotes',description="***I'm gonna give blowies at the orphanage*** -mazy\n\n***mazy, they're toddlers*** -BT\n\n***And?*** -mazy",color=0xFFFF00)
  await ctx.reply(embed=mazquotes)

 @commands.command(name='wholoveshim')
 async def wholoveshim(self,ctx):
  wholove = Embed(description='***NO ONE***',color=0xFFFF00)
  await ctx.reply(embed=wholove)
 
 @commands.command(name='War')
 async def War(self,ctx):
  war = Embed(title='War',description="***Just spend youth commiting war crimes*** -BT3025",color=0xFFFF00)
  await ctx.reply(embed=war)
 
 @commands.command(name='sewerslide')
 async def sewerslide(self,ctx):
  sewerslide = Embed(title='Sewerslide',description='***Haha you depressed bitch haha do it no balls***',color=0xFFFF00)
  await ctx.reply(embed=sewerslide)
 
 @commands.command(name='stfu')
 async def stfu(self,ctx):
  stfu = Embed(title='STFU',description="https://www.youtube.com/watch?v=KRB-iHGHSqk or https://www.youtube.com/watch?v=OLpeX4RRo28",color=0xFFFF00)
  await ctx.reply(embed=stfu)
 
 @commands.command(name='littlegirls')
 async def littlegirls(self,ctx):
  littlegirl = Embed(title='Little Girls',description="https://www.youtube.com/watch?v=6ltAVRyeqHk",color=0xFFFF00)
  await ctx.reply(embed=littlegirl)
 
 @commands.command(name='yeeyeehaircut')
 async def YeeYeeHaircut(self,ctx):
  yeeyeehc = Embed(title='Yee Yee Haircut',description="***Ah, nigga, don't hate me 'cause I'm beautiful, nigga. Maybe if you got rid of that old yee-yee ass haircut you got you'd get some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog-ass if she ever stop fuckin' with that brain surgeon or lawyer she fucking with. Niggaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa***",color=0xFFFF00)
  await ctx.reply(embed=yeeyeehc)
 
 @commands.command(name='thetruth')
 async def TheTruth(self,ctx):
  truth = Embed(title='Truthbomb',description="***Maybe Khans kill people without looking them in the face, but I ain't a fink, dig? You've made your last delivery, kid. Sorry you got twisted up in this scene. From where you're kneeling it must seem like an 18-carat run of bad luck. But, truth is... the game was rigged from the start.***",color=0xFFFF00)
  await ctx.reply(embed=truth)
 
 @commands.command(name='instantweebdepression')
 async def instantweebdepression(self,ctx):
  instaweebdep = Embed(title='Instant Weeb Depression',description="***Ash, I am very worried because I haven’t seen you and I don’t know if you are okay. You said to me before, “we live in different worlds,” but I am not sure if that is true. We are from different countries, and our skin and eyes are different colours. But so what? We are friends. Isn’t that enough? What else do we need? I am very happy I came to America. I made many friends here. Above all… I met you, Ash. You asked me many times if you scare me. But I never felt scared of you, not even once, From the first time I met you. Actually, I always felt that you are hurt, much more than me - that your spirit is wounded. I know you are much smarter than me, and bigger, and stronger - but even so.. I always wanted to protect you. Funny, isn’t it? But what did I want to protect you from? I think I wanted to protect you from your future. Because your fate was sweeping you away, like a flood. Do you remember telling me about the leopard in the Hemingway book? He died at the top of the mountain, and you said he knew he will never go back down. But I said you are not a leopard, and that you can change your future. It’s true, Ash. You can change your fate. You are not alone, Ash. I am with you. My soul is always with you. Sayonara, New York… Sayonara, America. … Ash, but I’m not saying “sayonara” to you.. because this isn’t goodbye. I know we’ll see each other again someday.. You are my best friend, Ash.***",color=0xFFFF00)
  await ctx.reply(embed=instaweebdep)
 
 @commands.command(name='caveman')
 async def caveman(self,ctx):
  caveman = Embed(title='OOGABOOGA',color=0xFFFF00)
  caveman.set_image(url="https://media.discordapp.net/attachments/814345735226785812/814682754079260712/image0.gif")
  await ctx.reply(embed=caveman)
 
 @commands.command(name='loser') 
 async def Loser(self,ctx):
  loser = Embed(title='What a loser',color=0xFFFF00)
  loser.set_image(url="https://media.discordapp.net/attachments/814345735226785812/814684633530499113/image0.png?width=420&height=401")
  await ctx.reply(embed=loser)

 @commands.command(name='bigtiddiesandtrauma')
 async def BigTiddiesAndTrauma(self,ctx):
  bigtittiesandtruama = Embed(title='Big Tiddies *and trauma*',color=0xFFFF00)
  bigtittiesandtruama.set_image(url='https://i.redd.it/19erqlus9rr21.jpg')
  await ctx.reply(embed=bigtittiesandtruama)

 @commands.command(name='lightningmcqueen')
 async def LightningMcqueen(self,ctx):
  lightningmcfuck = Embed(title='KACHOW',color=0xFFFF00)
  lightningmcfuck.set_image(url="https://i.ytimg.com/vi/3S6uNw-D6RA/maxresdefault.jpg")
  await ctx.reply(embed=lightningmcfuck)

 @commands.command(name='doinyamom')
 async def DoinYaMom(self,ctx):
  doinyamum = Embed(title="Doin ya mom",description="Doin ya mom",color=0xFFFF00)
  await ctx.reply(embed=doinyamum)

 @commands.command(name='nukes')
 async def Nukes(self,ctx):
  nukes = Embed(title='Nukes',description="***I am become death, destroyer of worlds***",color=0xFFFF00)
  await ctx.reply(embed=nukes)

 @commands.command(name='oath')
 async def Oath(self,ctx):
  oath = Embed(title='The Oath',description="***I, Barry B. Benson swear on my worthless bot life to say nothing but the truth***",color=0xFFFF00)
  await ctx.reply(embed=oath)

 @commands.command(name='bestgameever')
 async def BestGameEver(self,ctx):
  bestgamever = Embed(title='ALL BAD',description="***EVERY GAME EVER PLAYED IS A PIECE OF SHIT***",color=0xFFFF00)
  await ctx.reply(embed=bestgamever)
  
 @commands.command(name='retard')
 async def retard(self,ctx):
  retard = Embed(title="I found one!!!" ,color=0xFFFF00)
  retardimg = ctx.author.avatar_url
  retard.set_image(url=retardimg)
  await ctx.reply(embed=retard)

 @commands.command(name='pooper')
 async def pooper(self,ctx):
  poopie = Embed(title="That's one big stink",color=0xFFFF00)
  poopie.set_image(url='https://i.cbc.ca/1.4956283.1545425483!/fileImage/httpImage/image.JPG_gen/derivatives/16x9_780/trump-poo.JPG')
  await ctx.reply(embed=poopie)

 @commands.command(name='tractor')
 async def tractor(self,ctx):
  tractor = Embed(title='She likes my tractor',color=0xFFFF00)
  tractor.set_image(url='https://i.ytimg.com/vi/gaiOisHQSlQ/maxresdefault.jpg')
  await ctx.reply(embed=tractor)

 @commands.command(name='whois_urdad')
 async def whois_urdad(self,ctx):
  urdaddy = Embed(title='Fuckin weird redneck lookin ass',color=0xFFFF00)
  urdaddy.set_image(url='https://static8.depositphotos.com/1386061/896/i/600/depositphotos_8963619-stock-photo-southern-hick-with-a-rifle.jpg') 
  await ctx.reply(embed=urdaddy)

 @commands.command(name='yeetusthatfetus')
 async def yeetusthatfetus(self,ctx):
  fetus = Embed(title='An ultra speedy abortion',color=0xFFFF00)
  fetus.set_image(url='https://i.pinimg.com/originals/cb/ce/fa/cbcefafdc787c75b12ddce68e47c753c.jpg')
  await ctx.reply(embed=fetus)

 @commands.command(name='im14andthisisdeep')
 async def im14andthisisdeep(self,ctx):
  deep = Embed(title='14 Year Old Girls Be Like:',color=0xFFFF00)
  deep.set_image(url='https://i.ytimg.com/vi/_Nu6_A6PXEY/maxresdefault.jpg')
  await ctx.reply(embed=deep)

 @commands.command(name='search')
 async def search(self,ctx, *, arg):
  try:
	  from googlesearch import search
  except ImportError:
   await ctx.reply("No module named 'google' found")
  for j in search(arg, tld="co.in", num=1, stop=1, pause=2):
	  await ctx.reply(j)

 @commands.command(name='hack')
 async def hack(self,ctx,user:discord.Member = (None)):
  homeworkfolder = [
   'Mom',
   'Dad',
   'Grandma',
   'Grandpa',
   'School',
  ]
  homeworkran = random.choice(homeworkfolder)
  if user is None:
   await ctx.reply('`Error: Needs a target to hack stupid`')
   return
  else:
   hackmsg = await ctx.reply("<a:redsiren:867615081084223529>**Starting the hack on {}.**<a:bluesiren:867615267386818570>".format(user))
   await asyncio.sleep(1)
   await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}..**<a:bluesiren:867615267386818570>".format(user))
   await asyncio.sleep(1)
   await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}...**<a:bluesiren:867615267386818570>".format(user))
   await asyncio.sleep(1)
   await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}.**<a:bluesiren:867615267386818570>".format(user))
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Finding info.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Finding info..**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Finding info...**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Finding info.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Email:** `{}@lemenmail.seggs`\n\n**Phone:** `(420) 690-6969`\n\n**Job:** `Verified Pornhub Actor`".format(user))
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Injecting malware.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Injecting malware..**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Injecting malware...**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Injecting malware.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="<:Nigeriancat:849547273339142154>**Access obtained**<:Nigeriancat:849547273339142154>")
   await asyncio.sleep(2)
   await hackmsg.edit(content="**Navigating to `C:\Homework`**")
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Planting gay furry porn.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Planting gay furry porn..**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Planting gay furry porn...**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Planting gay furry porn.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Planted**")
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Sharing the folder to {}**".format(homeworkran))
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Family successfully torn apart**")
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Looking through search history.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Looking through search history..**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Looking through search history...**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Looking through search history.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Most recent search:** `Pornhub.com: Glory Hole get used by them all`")
   await asyncio.sleep(3)
   await hackmsg.edit(content="**Destroying evidence.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Destroying evidence..**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Destroying evidence...**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**Destroying evidence.**")
   await asyncio.sleep(1)
   await hackmsg.edit(content="**The FBI is definately on your ass now so good luck**")
   await asyncio.sleep(3)
   await hackmsg.edit(content="**The hack is complete**")

 @commands.command(name='emoji')
 async def emoji(self,ctx, *, args):
  if args == ':wumpbongo:':
   await ctx.reply('<a:wumpbongo:799111582130110515>')
  if args == ':vibez:':
   await ctx.reply('<a:vibez:799108578920497172>')
  if args == ':rgblob:':
   await ctx.reply('<a:rgblob:798608769897463858>')
  if args == ':redsiren:':
   await ctx.reply('<a:redsiren:867615081084223529>')
  if args == ':popcat:':
   await ctx.reply('<a:popcat:799111068168224808>')
  if args == ':peacebruh:':
   await ctx.reply('<a:peacebruh:799108579051175936>')
  if args == ':knowledge:':
   await ctx.reply('<a:knowledge:801824327053737994>')
  if args == ':itwasme:':
   await ctx.reply('<a:itwasme:799111032575885342>')
  if args == ':hydrate:':
   await ctx.reply('<a:hydrate:818297802081435648>')
  if args == ':hornycord:':
   await ctx.reply('<a:hornycord:799111581900341270>')
  if args == ':Fsmash:':
   await ctx.reply('<a:Fsmash:799108579151708182>')
  if args == ':dino:':
   await ctx.reply('<a:dino:802596004938776646>')
  if args == ':danceblob:':
   await ctx.reply('<a:danceblob:799108578882486283>')
  if args == ':comeatme:':
   await ctx.reply('<a:comeatme:799112392264908810>')
  if args == ':bluesiren:':
   await ctx.reply('<a:bluesiren:867615267386818570>')
  if args ==':applecat:':
   await ctx.reply('<a:applecat:799111032705384498>')
  if args == ':animeroll:':
   await ctx.reply('<a:animeroll:799106437942345728>')