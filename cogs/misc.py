import discord
from discord.ext import commands
import datetime
import time
from random import choice , randint

color1 = discord.Color.from_rgb(93,71,82)
color2 = discord.Color.from_rgb(248,238,229)
color3 = discord.Color.from_rgb(228,188,148)
color4 = discord.Color.from_rgb(129,110,112)

randcol = [color1, color2, color3, color4]
melon = choice(randcol)
blacklistChannel = [725641711770009623]

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(aliases=['av'])
    # async def avatar(self, ctx,*, member:discord.Member=None):
    #     if ctx.channel.id in blacklistChannel:
    #         await ctx.reply("Don't Use That Command in General Chat")
    #         return
    #     if member is None:
    #         member = ctx.author
    #     emb = discord.Embed(title="Avatar" ,color=melon,description=f"`Nickname: {member.display_name}\nID: {member.id}`")
    #     emb.set_author(name=member, icon_url=member.avatar_url)
    #     emb.timestamp = datetime.datetime.utcnow()
    #     emb.set_footer(text=f"Requested by : {ctx.author}", icon_url=self.bot.user.avatar_url)
    #     emb.set_image(url=member.avatar_url)
    #     await ctx.send(embed=emb)

    @commands.command()
    async def botstats(self, ctx):
        emb = discord.Embed(title="__Amy Stats__", color=melon)
        emb.add_field(
            name="Total Servers", value=str(len(self.bot.guilds)), inline=False
        )
        emb.add_field(
            name="Latency(s)", value=str(round(self.bot.latency, 3)), inline=False
        )
        emb.add_field(
            name=f"{ctx.guild} members", value=f"{ctx.guild.member_count}", inline=False
        )
        await ctx.send(embed=emb)
    
    @commands.command()
    async def server(self, ctx):
        await ctx.send(f"__Support Server__:\n https://discord.gg/eZFKMmS6vz ")

    @commands.command()
    async def ping(self,ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")   
    

    @commands.command(aliases=['source'])
    async def github(self, ctx):
        await ctx.reply(f" <:amyBed:863681197577601024>UwU \nRepo Link :-https://github.com/dhanushlnaik/Amy-Sensei ")

    @commands.command(aliases=['about', 'userinfo'])
    async def whois(self, ctx, member: discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        if member is None:
            member = ctx.author
        created_at = member.created_at.strftime("%b %d, %Y")
        joined_at = member.joined_at.strftime("%b %d, %Y")
        rolesMention = [role.mention for role in member.roles]
        rolesMention.pop(0)
        rolesMention.reverse()
        noPermList =  ['Create Instant Invite',  'Add Reactions',  'Priority Speaker', 'Stream', 'Read Messages', 'Send Messages', 'Send TTS Messages', 'Embed Links', 'Attach Files', 'Read Message History', 'Connect', 'Speak',  'Use Voice Activation',  'Use Slash Commands', 'Request To Speak']
        permList = [p[0].replace('_',' ').replace('guild', 'server').title().replace('Tts','TTS') for p in member.guild_permissions if p[1]]
        
        for perm in noPermList:
            if perm in permList:
                permList.remove(perm)
        admin = False
        mod = False
        manager = False
        memberA=False
        if  "Administrator" in permList:
            admin = True
        elif "Manage Server" in permList:
            manager = True
        elif "Mute Members" in permList:
            mod = True
        else:
            memberA = True
        text=', '.join(permList)
        
        embed = discord.Embed(title="", description=member.mention, color=ctx.author.color)
        embed.add_field(name="Created", value=created_at)
        embed.add_field(name="Joined", value=joined_at)
        embed.add_field(name=f"Roles [{len(rolesMention)}]", value=" ".join(rolesMention), inline=False)
        if not memberA:
            embed.add_field(name="Key Permissions", value=text, inline=False)
        if admin:
            embed.add_field(name="Acknowledgements", value="Server Admin", inline=False)
        if manager:
            embed.add_field(name="Acknowledgements", value="Server Manager", inline=False)
        if mod:
            embed.add_field(name="Acknowledgements", value="Server Moderator", inline=False)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp =  datetime.datetime.utcnow()
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
    # @commands.command(pass_context=True)
    # @commands.has_permissions(manage_messages=True)
    # async def poll(self, ctx, question, *options: str):

    #     if len(options) > 10:
    #         await ctx.send('```Error! Max Poll Limit is 10! ```')
    #         return

    #     if len(options) == 2 and options[0] == "yes" and options[1] == "no":
    #         reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣",
    #     "🔟", "🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮"] 
    #     else:
    #         reactions  = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣",
    #     "🔟", "🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮"] 

    #     description = []
    #     for x, option in enumerate(options):
    #         description += '{} {}\n'.format(reactions[x], option)

    #     poll_embed = discord.Embed(title=question, color=0x31FF00, description=''.join(description))

    #     react_message = await ctx.send(embed=poll_embed)

    #     for reaction in reactions[:len(options)]:
    #         await react_message.add_reaction(reaction)

    @commands.command()
    async def invite(self,ctx):
        emb = discord.Embed(color = melon, description=f" [Click here](https://discord.com/api/oauth2/authorize?client_id=850243448724127754&permissions=939838544&scope=bot) to invite me :))")
        await ctx.send(embed=emb)

    @commands.command()
    async def upvote(self,ctx):
        emb = discord.Embed(color = melon, description=f" [Click here](https://top.gg/bot/850243448724127754/vote) to upvote me :))")
        emb.set_footer(icon_url=self.bot.user.avatar_url, text=f"UwU")
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Misc(bot))
 
 
