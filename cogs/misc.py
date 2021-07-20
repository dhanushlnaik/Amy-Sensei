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

    @commands.command(aliases=['av'])
    async def avatar(self, ctx,*, member:discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        if member is None:
            member = ctx.author
        emb = discord.Embed(title="Avatar" ,color=melon,description=f"`Nickname: {member.display_name}\nID: {member.id}`")
        emb.set_author(name=member, icon_url=member.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        emb.set_footer(text=f"Requested by : {ctx.author}", icon_url=self.bot.user.avatar_url)
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)

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
    

    @commands.command()
    async def github(self, ctx):
        await ctx.reply(f" Wait for Tatsuya to make repo Public :O")

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

def setup(bot):
    bot.add_cog(Misc(bot))
 
 