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
import requests
import praw
from utils import *
import urbandict

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
api_key = 'giphyApi Key'
imgur = ImgurClient('Client ID','Client Secret')

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
    async def random(self, ctx, subreddit: str = ""):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        async with ctx.channel.typing():
            if self.reddit:
                # start working
                nsfw_flag = False
                chosen_subreddit = REDDIT_ENABLED_MEME_SUBREDDITS[0]
                if subreddit:
                    chosen_subreddit = subreddit

                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("This is not allowed here")
                        return

                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick = randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else:
                await ctx.send("This is not working. Contact Administrator.")
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
    async def dare(self,ctx):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        dareRand = choice(DARE)
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"DARE : {dareRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def truth(self,ctx):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        dareRand = choice(TRUTH)
        emb = discord.Embed(color = melon)
        emb.set_author(name=f"TRUTH : {dareRand}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def urban(self,ctx,*,define):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        term = urbandict.define(define)
        ex = term[0]['example']
        meaning = term[0]['def']
        embed = discord.Embed(title=f"{define.title()}",description=f"Meaning : {meaning}",color=melon)
        embed.add_field(name="Example:", value=f"{ex}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(aliases=['mock'])
    async def drunkify(self, ctx, *, s):
        lst = [str.upper, str.lower]
        newText = await commands.clean_content().convert(ctx, ''.join(choice(lst)(c) for c in s))
        if len(newText) <= 380:
            await ctx.send(newText)
        else:
            try:
                await ctx.author.send(newText)
                await ctx.send(f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**")
            except Exception:
                await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")


    @commands.command()
    async def ship(self, ctx, name1 : commands.clean_content, name2 : commands.clean_content):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            pass
        shipnumber = randint(0,100)
        if 0 <= shipnumber <= 10:
            status = "Really low! {}".format(choice(["Friendzone ;(", 
                                                            'Just "friends"', 
                                                            '"Friends"', 
                                                            "Little to no love ;(", 
                                                            "There's barely any love ;("]))
        elif 10 < shipnumber <= 20:
            status = "Low! {}".format(choice(["Still in the friendzone", 
                                                     "Still in that friendzone ;(", 
                                                     "There's not a lot of love there... ;("]))
        elif 20 < shipnumber <= 30:
            status = "Poor! {}".format(choice(["But there's a small sense of romance from one person!", 
                                                     "But there's a small bit of love somewhere", 
                                                     "I sense a small bit of love!", 
                                                     "But someone has a bit of love for someone..."]))
        elif 30 < shipnumber <= 40:
            status = "Fair! {}".format(choice(["There's a bit of love there!", 
                                                      "There is a bit of love there...", 
                                                      "A small bit of love is in the air..."]))
        elif 40 < shipnumber <= 60:
            status = "Moderate! {}".format(choice(["But it's very one-sided OwO", 
                                                          "It appears one sided!", 
                                                          "There's some potential!", 
                                                          "I sense a bit of potential!", 
                                                          "There's a bit of romance going on here!", 
                                                          "I feel like there's some romance progressing!", 
                                                          "The love is getting there..."]))
        elif 60 < shipnumber <= 70:
            status = "Good! {}".format(choice(["I feel the romance progressing!", 
                                                      "There's some love in the air!", 
                                                      "I'm starting to feel some love!"]))
        elif 70 < shipnumber <= 80:
            status = "Great! {}".format(choice(["There is definitely love somewhere!", 
                                                       "I can see the love is there! Somewhere...", 
                                                       "I definitely can see that love is in the air"]))
        elif 80 < shipnumber <= 90:
            status = "Over average! {}".format(choice(["Love is in the air!", 
                                                              "I can definitely feel the love", 
                                                              "I feel the love! There's a sign of a match!", 
                                                              "There's a sign of a match!", 
                                                              "I sense a match!", 
                                                              "A few things can be imporved to make this a match made in heaven!"]))
        elif 90 < shipnumber <= 100:
            status = "True love! {}".format(choice(["It's a match!", 
                                                           "There's a match made in heaven!", 
                                                           "It's definitely a match!", 
                                                           "Love is truely in the air!", 
                                                           "Love is most definitely in the air!"]))

        if shipnumber <= 33:
            shipColor = 0xE80303
        elif 33 < shipnumber < 66:
            shipColor = 0xff6600
        else:
            shipColor = 0x3be801

        emb = (discord.Embed(color=shipColor, \
                             title="Love test for:", \
                             description="**{0}** and **{1}** {2}".format(name1, name2, choice([
                                                                                                        ":sparkling_heart:", 
                                                                                                        ":heart_decoration:", 
                                                                                                        ":heart_exclamation:", 
                                                                                                        ":heartbeat:", 
                                                                                                        ":heartpulse:", 
                                                                                                        ":hearts:", 
                                                                                                        ":blue_heart:", 
                                                                                                        ":green_heart:", 
                                                                                                        ":purple_heart:", 
                                                                                                        ":revolving_hearts:", 
                                                                                                        ":yellow_heart:", 
                                                                                                        ":two_hearts:"]))))
        emb.add_field(name="Results:", value=f"{shipnumber}%", inline=True)
        emb.add_field(name="Status:", value=(status), inline=False)
        emb.set_author(name="Shipping", icon_url="http://moziru.com/images/kopel-clipart-heart-6.png")
        await ctx.send(embed=emb)
        
    @commands.command(aliases=["8ball", "tellme"])
    async def eightball(self, ctx, *, _ballInput: commands.clean_content):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        """extra generic just the way you like it"""
        choiceType = choice(["(Affirmative)", "(Non-committal)", "(Negative)"])
        if choiceType == "(Affirmative)":
            prediction = choice(["It is certain ", 
                                        "It is decidedly so ", 
                                        "Without a doubt ", 
                                        "Yes, definitely ", 
                                        "You may rely on it ", 
                                        "As I see it, yes ",
                                        "Most likely ", 
                                        "Outlook good ", 
                                        "Yes ", 
                                        "Signs point to yes "]) + ":8ball:"

            emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0x3be801, description=prediction))
        elif choiceType == "(Non-committal)":
            prediction = choice(["Reply hazy try again ", 
                                        "Ask again later ", 
                                        "Better not tell you now ", 
                                        "Cannot predict now ", 
                                        "Concentrate and ask again "]) + ":8ball:"
            emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0xff6600, description=prediction))
        elif choiceType == "(Negative)":
            prediction = choice(["Don't count on it ", 
                                        "My reply is no ", 
                                        "My sources say no ", 
                                        "Outlook not so good ", 
                                        "Very doubtful "]) + ":8ball:"
            emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0xE80303, description=prediction))
        emb.set_author(name='Magic 8 ball', icon_url='https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png')
        await ctx.send(embed=emb)


    @commands.command(aliases=['gay-scanner', 'gayscanner', 'gay'])
    async def gay_scanner(self, ctx,* ,user: commands.clean_content=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        if not user:
            user = ctx.author.name
        gayness = randint(0,100)
        if gayness <= 33:
            gayStatus = choice(["No homo", 
                                       "Wearing socks", 
                                       '"Only sometimes"', 
                                       "Straight-ish", 
                                       "No homo bro", 
                                       "Girl-kisser", 
                                       "Hella straight"])
            gayColor = 0xFFC0CB
        elif 33 < gayness < 66:
            gayStatus = choice(["Possible homo", 
                                       "My gay-sensor is picking something up", 
                                       "I can't tell if the socks are on or off", 
                                       "Gay-ish", 
                                       "Looking a bit homo", 
                                       "lol half  g a y", 
                                       "safely in between for now"])
            gayColor = 0xFF69B4
        else:
            gayStatus = choice(["LOL YOU GAY XDDD FUNNY", 
                                       "HOMO ALERT", 
                                       "MY GAY-SENSOR IS OFF THE CHARTS", 
                                       "STINKY GAY", 
                                       "BIG GEAY", 
                                       "THE SOCKS ARE OFF", 
                                       "HELLA GAY"])
            gayColor = 0xFF00FF
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"{gayness}% gay")
        emb.add_field(name="Comment:", value=f"{gayStatus} :kiss_mm:")
        emb.set_author(name="Gay-Scanner™", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
        await ctx.send(embed=emb)
def setup(bot):
    bot.add_cog(Fun(bot))
 