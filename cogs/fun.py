import discord
from discord.ext import commands
import datetime
import time
from random import choice , randint
from asyncio import TimeoutError
from discord_components import *
from json import loads
from aiohttp import ClientSession
from imgurpython import ImgurClient
import giphy_client
from giphy_client.rest import ApiException
from requests import get
import praw
from utils import *
import urbandict


response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
quote = '{quoteText} - {quoteAuthor}'.format(**loads(response.text))

blacklistChannel = [725641711770009623]

REDDIT_APP_ID = ''
REDDIT_APP_SECRET = ''
REDDIT_ENABLED_MEME_SUBREDDITS = [
    'funny',
    'memes'
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'wtf'
]

def user_is_me(ctx):
    return ctx.message.author.id == 624174437821972480
# __COLORS__
color1 = discord.Color.from_rgb(93,71,82)
color2 = discord.Color.from_rgb(248,238,229)
color3 = discord.Color.from_rgb(228,188,148)
color4 = discord.Color.from_rgb(129,110,112)

randcol = [color1, color2, color3, color4]
melon = choice(randcol)


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)

tenor_key = ''
api_key = ''
imgur = ImgurClient('','')

async def get(session: object, url: object) -> object:
        async with session.get(url) as response:
            return await response.text()


rpsC = ["Rock", "Paper", "Scissors"]
melon = discord.Color.from_rgb(248,131,121)
response_list = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Gino's mom told me yes", "Gino's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET,
                                      user_agent="ULTIMATE_DISCORD_BOT:%s:1.0" % REDDIT_APP_ID)

    @commands.command()
    async def random(self, ctx, subreddit: str="anime"):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        async with ctx.channel.typing():
            if self.reddit:
                allsubs = []
                submissions = self.reddit.subreddit(subreddit)
                top = submissions.top(limit=50)
                for subm in top:
                    allsubs.append(subm)

                randomsub = choice(allsubs)

                while True:
                    name = randomsub.title
                    url = randomsub.url
                    if url.endswith("jpg") or url.endswith("png"):
                        break
                    else:
                        randomsub = choice(allsubs)
                em = discord.Embed(title=name, color=discord.Color.blurple())
                em.set_image(url=url)
                await ctx.send(embed=em)
            else:
                await ctx.send("This is not working. Contact Administrator.")

    @commands.command(brief="You Momma is!")
    async def insult(self, ctx, member: discord.Member = None):
        insult = get_momma_jokes()
        if member is not None:
            await ctx.send("%s eat this: %s " % (member.name, insult))
        else:
            await ctx.send("%s for yourself: %s " % (ctx.message.author.name, insult))

    @commands.command()
    @commands.check(user_is_me)
    async def say(self, ctx,*,msg):
        if "discord.gg" in msg:
            await ctx.reply("You Bad :/")
        else:
            await ctx.send(msg)
            await ctx.message.delete()
    @commands.command()
    async def rps(self, ctx):

        rpsC = ["Rock", "Paper", "Scissors"]
        comp = choice(rpsC)
        yet = discord.Embed(title=f"{ctx.author.display_name}'s RPS Game!", description=f">>> You haven't clicked on any button yet!", color=melon)
        win = discord.Embed(title=f"{ctx.author.display_name}, You Won!", description=f">>> You have won! My Choice was `{comp}` :(", color=discord.Color.green())
        lost = discord.Embed(title=f"{ctx.author.display_name}, You Lost!", description=f">>> You have Lost! My Choice was `{comp}` Haha!", color=discord.Color.red())
        out = discord.Embed(title=f"{ctx.author.display_name}, You didn't Click on Time", description=f">>> Time Out! ", color=discord.Color.red())
        tie = discord.Embed(title=f"{ctx.author.display_name}, Tie!", description=f">>> It's a Tie! My Choice was `{comp}`", color=melon)
        m = await ctx.send(
            embed=yet,
            components=[[Button(style=ButtonStyle.grey, label="Rock", emoji="🥌"),Button(style=ButtonStyle.green, label="Paper", emoji="📃"),Button(style=ButtonStyle.red, label="Scissors", emoji="✂")]]
        )
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            res = await self.bot.wait_for("button_click", check=check,timeout=10)
            player = res.component.label

            if player == comp:
                await m.edit(embed=tie,components=[])
            if player == "Rock" and comp == "Paper":
                await m.edit(embed=lost,components=[])
            if player == "Rock" and comp == "Scissors":
                await m.edit(embed=win,components=[])
            if player == "Paper" and comp == "Rock":
                await m.edit(embed=win,components=[])
            if player == "Paper" and comp == "Scissors":
                await m.edit(embed=lost,components=[])
            if player == "Scissors" and comp == "Rock":
                await m.edit(embed=lost,components=[])
            if player == "Scissors" and comp == "Paper":
                await m.edit(embed=win,components=[])
        except TimeoutError:
            await m.edit(embed=out,components=[Button(label="Oops", disabled=True)])

    @commands.command()
    async def dog(self, ctx):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        async with ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()

        embed = discord.Embed(title="Doggo!", color=discord.Color.purple(), description=factjson['fact'])
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        async with ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            dogjson = await request.json()
            # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()

        embed = discord.Embed(title="Cat", color=discord.Color.purple(), description=factjson['fact'])
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)


    @commands.command()
    async def imgur(self, ctx, *text: str):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        """Allows the user to search for an image from imgur"""
        rand = randint(0, 29)
        if text == ():
            await ctx.send('**Please enter a search term**')
        elif text[0] != ():
            items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='viral', window='all',page=0)
            await ctx.send(items[rand].link)

    @commands.command()
    async def gif(self, ctx,*,q="Anime"):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            rgiff = choice(lst)
            emb = discord.Embed(color=ctx.author.color)
            emb.set_author(name=q.title(),icon_url=ctx.author.avatar_url)
            emb.set_image(url=f"https://media.giphy.com/media/{rgiff.id}/giphy.gif")
            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling Api as "+e)

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
            await ctx.message.delete()
        else:
            await ctx.send("Please use @mention to poke someone.")
            
    @commands.command(brief="Any message to owo")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command()
    async def dare(self,ctx,*,msg=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        dareRand = get_dare()
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"DARE : {dareRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def truth(self,ctx,*,msg=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        truthRand = get_truth()
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"TRUTH : {truthRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def wyr(self,ctx,*,msg=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        wyrRand = get_wyr()
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"{wyrRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def nhie(self,ctx,*,msg=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        nhieRand = get_nhie()
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"{nhieRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def urban(self,ctx,*,define):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        term = urbandict.define(define)
        print(term)
        ex = term[0]['example']
        meaning = term[0]['def']
        embed = discord.Embed(title=f"{define.title()}",description=f"Meaning : {meaning}\n {term[1]['def']}",color=melon)
        embed.add_field(name="Example:", value=f"{ex}\n{term[1]['example']}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=["motivate", "quote"])
    async def quo(self,ctx):
        from random_word import RandomWords
        from quote import quote
        r = RandomWords()
        w = r.get_random_word()
        
        res = quote(w, limit=1)
        for i in range(len(res)):
            quote = f"{res[i]['quote']}\n-{res[i]['quote']}"
        await ctx.send(quote)

    @commands.command(aliases=["jokes"])
    async def joke(self,ctx):
        def jokes(f):

            data = get(f)
            tt = loads(data.text)
            return tt

        f = r"https://official-joke-api.appspot.com/jokes/programming/random"
        a = jokes(f)

        for i in (a):
            mainJ = i["setup"]
            punchL = i["punchline"]
            await ctx.send(f"{mainJ}/n/n ||{punchL}||")


def setup(bot):
    bot.add_cog(Fun(bot))
 
