# __IMPORTS__
import discord 
from discord.ext import commands
from oauth2client.client import Error
import pyrebase
from json import  load 
import datetime
from db import *
from discord_components import *
import asyncio
import random
import urbandict
blacklistChannel = [725641711770009623]
"""
<UserRelationship>
                        Waifuu Id :0 ;
                        Children:0;
                        Siblings :0;
                        Parent :0;
                        DOM :0;
                        Days:0;
"""

# __COLORS__
color1 = discord.Color.from_rgb(93,71,82)
color2 = discord.Color.from_rgb(248,238,229)
color3 = discord.Color.from_rgb(228,188,148)
color4 = discord.Color.from_rgb(129,110,112)

randcol = [color1, color2, color3, color4]
melon = random.choice(randcol)

# FUNCTIONS
with open("firebase.json", "r") as read_file:
    firebase = pyrebase.initialize_app(load(read_file))
db = firebase.database()

def new_member(member_id: int):
    db.child("UserRelationship").child(member_id).set(
        {"Relationship": "0", "Siblings":"0", "DOM":"0", "Days":"0"})

def add_relationship(member_id: int, relationship: str, rel_Id:str):
    guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    if guild_relationship == None:
        new_member(member_id)
    guild_relationship[relationship] = rel_Id
    db.child("UserRelationship").child(member_id).set(guild_relationship)

def add_sibling(member_id: int, rel_Id:str):
    guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    if guild_relationship["Siblings"] == "0":
        guild_relationship["Siblings"] = str(rel_Id)
    else:
        guild_relationship["Siblings"] = str(guild_relationship["Siblings"])+ "," + str(rel_Id)
    db.child("UserRelationship").child(member_id).set(guild_relationship)

def add_time(member_id: int):
    guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    if guild_relationship == None:
        new_member(member_id)
        guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    
    guild_relationship["DOM"] = str(datetime.datetime.now().strftime("%a, %B %d,%Y"))
    db.child("UserRelationship").child(member_id).set(guild_relationship)
    guild_relationship["Days"] = str(datetime.date.today())
    db.child("UserRelationship").child(member_id).set(guild_relationship)

def rmv_time(member_id: int):
    guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    if guild_relationship == None:
        new_member(member_id)
        guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    
    guild_relationship["DOM"] = "0"
    db.child("UserRelationship").child(member_id).set(guild_relationship)
    guild_relationship["Days"] = "0"
    db.child("UserRelationship").child(member_id).set(guild_relationship)
    
def check_relationship(member_id: int,relationship: str ):
    guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    if guild_relationship == None:
        new_member(member_id)
        guild_relationship = db.child("UserRelationship").child(member_id).get().val()
    relation = guild_relationship[relationship]
    return relation

def is_sibling(rel1:str, rel2: str):
    rel = str(check_relationship(int(rel1),"Siblings"))
    print(rel)
    q= rel.split(",")
    if str(rel2) in q:
        return True
    else:
        return False

def remv_sib(rel1:int, rel2:str):
    guild_relationship = db.child("UserRelationship").child(rel1).get().val()
    li = guild_relationship["Siblings"].split(',')
    if rel2 in li:
        li.remove(rel2)
        guild_relationship["Siblings"] = ','.join(li)
        db.child("UserRelationship").child(rel1).set(guild_relationship)
    else:
        return
    

class MarrySys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def marry(self, ctx, user: discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return

        prefix = check_prefix(ctx.guild.id)

        if user is None:
            rel = int(check_relationship(ctx.author.id,"Relationship"))

            if int(rel) is 0:
                emb=discord.Embed(description=f"{ctx.author.name}, you are not married! Please marry Someone First! ex. `{prefix}marry @user` ", color=melon)
                emb.set_author(name="You're not currently married.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=emb)
            else:
                dat = check_relationship(ctx.author.id,"DOM")
                today = datetime.datetime.today()
                some = check_relationship(ctx.author.id, "Days")
                someday = datetime.datetime.strptime(some ,'%Y-%m-%d')
                diff = today - someday
                ppl = discord.utils.get(self.bot.get_all_members(), id=rel)
                emb=discord.Embed(description=f"Married since {dat} ({diff.days} days), !The perfect pair! <3 ", color=melon)
                emb.set_author(name=f"{ctx.author.name}, you are happily married to {ppl.name}", icon_url=ctx.author.avatar_url)
                emb.set_thumbnail(url="https://i.gifer.com/ZdPB.gif")
                await ctx.send(embed=emb)
        elif not user.bot:
            if ctx.author.id ==user.id:
              await ctx.reply("Sad Soul!! You can't marry Yourself!")
              return
            if is_sibling(ctx.author.id, user.id):
                await ctx.reply("https://cdn.discordapp.com/attachments/855321779001884682/865241148943761418/Sweet_home_Alabama_ukelele.webm")
                await ctx.send(f":no_entry_sign: | **{ctx.author.name}** , you can't marry your sibling!!")
                return
            rel = int(check_relationship(ctx.author.id,"Relationship"))
            rel2 = int(check_relationship(user.id,"Relationship"))
            if rel == 0 and rel2 == 0 and not is_sibling(ctx.author.id, user.id):
                emb = discord.Embed(description=f"Hey, {user.mention}, it would make {ctx.author.mention} really happy if you would marry them. What do you say?\n", color=melon)
                emb.set_author(name=f"{ctx.author.name} has proposed to {user.name}! <3 ")
                emb.timestamp = datetime.datetime.utcnow()
                msg = await ctx.send(embed=emb,
            components=[
                [
                    Button(style=ButtonStyle.green, label="Yes!!", emoji="😳"),
                    Button(style=ButtonStyle.red, label="No ;-;", emoji="😔")],],)
                def check(res):
                    return user == res.user and res.channel == ctx.channel
                try:
                    res = await self.bot.wait_for("button_click", check=check,timeout=120)
                    player = res.component.label

                    if "yes"in player.lower():
                        await msg.edit( components=[])
                        await ctx.send(f"💒 || {ctx.author.mention} and {user.mention} are now married! Congrats!!|")
                        add_relationship(ctx.author.id,"Relationship",str(user.id ))
                        add_relationship(user.id,"Relationship",str(ctx.author.id ))
                        add_time(int(user.id))
                        add_time(int(ctx.author.id))
                        return
                    else:
                        await msg.edit(components=[])
                        await ctx.send(f"💔 || {user.mention}, you have decline a marriage request to {ctx.author.mention}")
                        return
                except asyncio.TimeoutError:
                    await msg.edit(components=[Button(label="Oops", disabled=True)])
                    await ctx.send(f"😠 || Sorry, {ctx.author.mention}, {user.name} didn't reply on time!! Maybe They are confused, lets give them some time!")
                    return
            elif rel == 0 and rel2 != 0 or rel != 0 and rel2 == 0:
                await ctx.reply(f":no_entry_sign: | **{ctx.author.name}** , you or your friend is already married!" ,components=[
        [
            Button(style=ButtonStyle.grey, label="Press F", emoji="❕", disabled=True)],],)
            else:
                return
        else:
            await ctx.reply("BRUH!! You can't Marry a bot!!\n `it's illegal`")
            return

    @commands.command()
    async def div(self,ctx):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        prefix = check_prefix(ctx.guild.id)
        rel = int(check_relationship(ctx.author.id,"Relationship"))
        if rel == 0:
            await ctx.reply(f":no_entry_sign: | {ctx.author.mention}, you can't divorce if you aren't married!")
            return
        else:
            try:
                ppl = discord.utils.get(self.bot.get_all_members(), id=rel)
                dat = check_relationship(ctx.author.id,"DOM")
                today = datetime.datetime.today()
                some = check_relationship(ctx.author.id, "Days")
                someday = datetime.datetime.strptime(some ,'%Y-%m-%d')
                diff = today - someday
                
                emb=discord.Embed(description=f"You married on {dat} and have been married for {diff.days} days... Once you divorce, the ring will break and disappear.", color=melon)
                emb.set_author(name=f"{ctx.author.name}, are you sure you want to divorce {ppl.name}?", icon_url=ctx.author.avatar_url)
                emb.set_thumbnail(url="https://i.gifer.com/ZdPB.gif")
                msg = await ctx.send(embed=emb, components=[
                [
                    Button(style=ButtonStyle.red, label="Yes ;-;", emoji="✔"),
                    Button(style=ButtonStyle.green, label="No ;-;", emoji="🚫")],],)
                def check(res):
                    return ctx.author == res.user and res.channel == ctx.channel
                try:
                    res = await self.bot.wait_for("button_click", check=check,timeout=60)
                    player = res.component.label

                    if "yes"in player.lower():
                        await msg.edit( components=[])
                        await ctx.send(f":broken_heart:  || {ctx.author.mention}, You have decided to divorce.")
                        add_relationship(ctx.author.id,"Relationship","0")
                        add_relationship(ppl.id,"Relationship","0")
                        rmv_time(int(ppl.id))
                        rmv_time(int(ctx.author.id))
                        return
                    else:
                        await msg.edit(components=[])
                        await ctx.send(f"👍 || {ctx.author.mention},You have declined to divorce.")
                        return
                except asyncio.TimeoutError:
                    await msg.edit(components=[Button(label="Oops", disabled=True)])
                    await ctx.send(f"😠 || Sorry, {ctx.author.mention} you didn't reply on time!!")
                    return
            except:
                return

    @commands.command(aliases=["sib"])
    async def rakhi(self, ctx, user: discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        prefix = check_prefix(ctx.guild.id)
        if user is None:
            rel = str(check_relationship(ctx.author.id,"Siblings"))
            sib = rel.split(",")
            desc = ""
            if rel == "0":
                emb=discord.Embed(description=f"{ctx.author.name}, You have no E-siblings right now! Please make Someone First! ex. `{prefix}sib @user` ", color=melon)
                emb.set_author(name="Lonely Soul", icon_url=ctx.author.avatar_url)
                emb.set_thumbnail(url="https://i.pinimg.com/originals/b3/8e/27/b38e27402bc8accd4e9b313a1b567fa6.gif")
                await ctx.send(embed=emb)
                return
            if len(sib) is 1:
                ppl = discord.utils.get(self.bot.get_all_members(), id=int(rel))
                emb=discord.Embed(description=f"▪️ {ppl.name} `({ppl.id})`", color=melon)
                emb.set_author(name=f"{ctx.author.name}, you have {len(sib)} Siblings : ", icon_url=ctx.author.avatar_url)
                emb.set_thumbnail(url="https://4.bp.blogspot.com/-T2bVs6xiUks/XHeLMCZlvOI/AAAAAAAUQDU/k-8YrZmX5j4S9VOaOULzqtExdduBcfPtQCLcBGAs/s1600/AW3567431_10.gif")
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                await ctx.send(embed=emb)
                return
            else:
                for a in range(len(sib)):
                    try:
                        print(sib[a])
                        ppl = discord.utils.get(self.bot.get_all_members(), id=int(sib[a]))
                        desc = desc + f"▪️ {ppl.name} `({ppl.id})`\n"
                    except Exception as e:
                        print(e)

                emb=discord.Embed(description=f"{desc}\n >>> `Foolo ka Taaron Ka Sabka Kehna hai!`", color=melon)
                emb.set_author(name=f"{ctx.author.name}, you have {len(sib)} siblings : ", icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                emb.set_thumbnail(url="https://4.bp.blogspot.com/-T2bVs6xiUks/XHeLMCZlvOI/AAAAAAAUQDU/k-8YrZmX5j4S9VOaOULzqtExdduBcfPtQCLcBGAs/s1600/AW3567431_10.gif")
                await ctx.send(embed=emb)
                return
        if ctx.author.id ==user.id:
            await ctx.reply("Sad Soul!!")
            return
        elif not user.bot:
            rel = str(check_relationship(ctx.author.id,"Siblings"))
            rel2 = str(check_relationship(user.id,"Siblings"))
            mar1 = int(check_relationship(ctx.author.id,"Relationship"))
            mar2 = int(check_relationship(user.id,"Relationship"))
            sib = rel.split(",")
            
            sib2 = rel2.split(",")
            if mar1 == mar2:
                await ctx.reply(f"🚫 If you wanna SiblingZone Someone, first Disown them!")
                return
            if rel == "0" and rel2=="0" or str(user.id) not in sib and str(ctx.author.id) not in sib2 :
                emb = discord.Embed(description=f"Hey {user.mention},  I feel glad too say that {ctx.author.mention} wants to make you their sibling ! It would make them  really happy if you accept this proposal. What do you say?\n")
                emb.set_author(name=f"{ctx.author.name} wants to make {user.name} their Sibling! <3 ")
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/865570883170861077/865875381537734686/output-onlinegiftools.gif")
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                msg = await ctx.send(embed=emb,
            components=[
                [
                    Button(style=ButtonStyle.green, label="Sure!!", emoji="😃"),
                    Button(style=ButtonStyle.red, label="No ;-;", emoji="😔")],],)
                def check(res):
                    return user == res.user and res.channel == ctx.channel
                try:
                    res = await self.bot.wait_for("button_click", check=check,timeout=120)
                    player = res.component.label

                    if "sure"in player.lower():
                        await msg.edit( components=[])
                        await ctx.send(f"🏡 || {user.mention}, Yay! {ctx.author.mention} is now your Sibling. Congrats!!")
                        add_sibling(ctx.author.id, user.id)
                        add_sibling(user.id,ctx.author.id )
                        return
                    else:
                        await msg.edit(components=[])
                        await ctx.send(f"💔 || {ctx.author.mention} Sorry ! But {user.mention} declined your request :((")
                        return
                except asyncio.TimeoutError:
                    await msg.edit(components=[Button(label="Oops", disabled=True)])
                    await ctx.send(f"😠 || Sorry, {ctx.author.mention}, {user.name} didn't reply on time!! Maybe They are confused, lets give them some time!")
                    return
            else:
                await ctx.reply(f"You Guys are Already Siblings !")
                return
        else:
            await ctx.reply("BRUH!! You can't make a bot your Sibling!!")

    @commands.command(aliases=["nosib", "disown"])
    async def remvsib(self,ctx, user: discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        prefix = check_prefix(ctx.guild.id)
        try:
            rel = int(check_relationship(ctx.author.id,"Siblings"))
        except:
            rel = check_relationship(ctx.author.id,"Siblings")
        if rel == 0:
            await ctx.reply(f"{ctx.author.name}, You have no E-siblings right now! Please make Someone First! ex. `{prefix}sib @user`")
            return
        if user is None:
            await ctx.send("Please use @mention  someone.")
            return
        else:
            try:
                guild_relationship = db.child("UserRelationship").child(ctx.author.id).get().val()
                li = guild_relationship["Siblings"].split(',')
                print(li)
                if str(user.id) in li:
                    emb=discord.Embed(description=f"{ctx.author.mention}, Are you sure? ", color=melon)
                    emb.set_author(name=f"{ctx.author.name}, are you sure you want to disown {user.name} as your Sibling?", icon_url=ctx.author.avatar_url)
                    
                    msg = await ctx.send(embed=emb, components=[
                    [
                        Button(style=ButtonStyle.red, label="Yes ;-;", emoji="✔"),
                        Button(style=ButtonStyle.green, label="No ;-;", emoji="🚫")],],)
                    def check(res):
                        return ctx.author == res.user and res.channel == ctx.channel
                    try:
                        res = await self.bot.wait_for("button_click", check=check,timeout=60)
                        player = res.component.label

                        if "yes"in player.lower():
                            await msg.edit( components=[])
                            await ctx.send(f":broken_heart:  || {ctx.author.mention}, You have decided to disown them as sibling.")
                            remv_sib(ctx.author.id, str(user.id))
                            remv_sib(user.id, str(ctx.author.id))
                            return
                        else:
                            await msg.edit(components=[])
                            await ctx.send(f"👍 || {ctx.author.mention},You have declined")
                            return
                    except asyncio.TimeoutError:
                        await msg.edit(components=[Button(label="Oops", disabled=True)])
                        await ctx.send(f"😠 || Sorry, {ctx.author.mention}, {user.name} didn't reply on time!! Maybe They are confused, lets give them some time!")
                        return
                else:
                    await ctx.reply(f"{ctx.author.name}, They are not your Sibling!")
                    return
            except:
                return

    @commands.command()
    async def family(self,ctx, user: discord.Member=None):
        if ctx.channel.id in blacklistChannel:
            await ctx.reply("Don't Use That Command in General Chat")
            return
        prefix = check_prefix(ctx.guild.id)
        if user is None:
            rel = str(check_relationship(ctx.author.id,"Siblings"))
            sib = rel.split(",")
            print(sib)
            desc = ""
            if rel == "0":
                desc = "You have no E-siblings right now!"
                lensib = "0"
            elif len(sib) is 1:
                ppl = discord.utils.get(self.bot.get_all_members(), id=int(rel))
                desc= f"▪️ {ppl.name} `({ppl.id})`"
                lensib=f"{len(sib)}"
            else:
                for a in range(len(sib)):
                    lensib = len(sib)
                    try:
                        print(sib[a])
                        ppl = discord.utils.get(self.bot.get_all_members(), id=int(sib[a]))
                        desc = desc + f"▪️ {ppl.name} `({ppl.id})`\n"
                    except Exception as e:
                        print(e)
            mar = int(check_relationship(ctx.author.id,"Relationship"))

            if int(mar) is 0:
                marLIst = f"You are not married! Please marry Someone First! ex. `{prefix}marry @user`"
            else:
                ppl = discord.utils.get(self.bot.get_all_members(), id=mar)
                marLIst = f" {ppl.name} `({ppl.id})`"
            if len(sib) < 20:
                emb=discord.Embed( color=ctx.author.color,description=f"`Nickname: {ctx.author.display_name}\nID: {ctx.author.id}`")
                emb.set_author(name=f"{ctx.author.name}'s Family", icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                emb.add_field(name=f"💞 Partner :", value=f" {marLIst}💓",inline=False)
                emb.add_field(name=f"❣ Siblings[{lensib}] :", value=f"{desc}",inline=False)
                emb.set_image(url="https://giffiles.alphacoders.com/113/113317.gif")
                await ctx.send(embed=emb)
                return
            else:
                emb=discord.Embed(color=ctx.author.color,description=f"`Nickname: {ctx.author.display_name}\nID: {ctx.author.id}`")
                emb.set_author(name=f"{ctx.author.name}'s Family", icon_url=ctx.author.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                emb.add_field(name=f"💞 Partner :", value=f" {marLIst}💓",inline=False)
                await ctx.send(embed=emb)
                embed=discord.Embed(color=ctx.author.color,description=f"**❣ Siblings[{lensib}] :**\n{desc}")
                embed.set_author(name=f"{ctx.author.name}'s Siblings", icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(icon_url=self.bot.user.avatar_url)
                embed.set_image(url="https://giffiles.alphacoders.com/113/113317.gif")
                await ctx.send(embed=embed)
                return
        else:
            rel = str(check_relationship(user.id,"Siblings"))
            sib = rel.split(",")
            desc = ""
            if rel == "0":
                desc = "They have no E-siblings right now!"
                lensib = "0"
            elif len(sib) is 1:
                ppl = discord.utils.get(self.bot.get_all_members(), id=int(rel))
                desc= f"▪️ {ppl.name} `({ppl.id})`"
                lensib=f"{len(sib)}"
            else:
                for a in range(len(sib)):
                    lensib = len(sib)
                    try:
                        print(sib[a])
                        ppl = discord.utils.get(self.bot.get_all_members(), id=int(sib[a]))
                        desc = desc + f"▪️ {ppl.name} `({ppl.id})`\n"
                    except:
                        print("hmm")
                        
            mar = int(check_relationship(user.id,"Relationship"))

            if int(mar) == 0:
                marLIst = f"They are not married! Please marry Someone First! ex. `{prefix}marry @user`"
            else:
                ppl = discord.utils.get(self.bot.get_all_members(), id=mar)
                marLIst = f"{ppl.name} `({ppl.id})`"

            if len(sib) < 20:
                emb=discord.Embed( color=user.color,description=f"`Nickname: {user.display_name}\nID: {user.id}`")
                emb.set_author(name=f"{user.name}'s Family", icon_url=user.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                emb.add_field(name=f"💞 Partner :", value=f" {marLIst}💓",inline=False)
                emb.add_field(name=f"❣ Siblings[{lensib}] :", value=f"{desc}",inline=False)
                emb.set_image(url="https://giffiles.alphacoders.com/113/113317.gif")
                await ctx.send(embed=emb)
                return
            else:
                emb=discord.Embed(color=user.color,description=f"`Nickname: {user.display_name}\nID: {user.id}`")
                emb.set_author(name=f"{user.name}'s Family", icon_url=user.avatar_url)
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(icon_url=self.bot.user.avatar_url)
                emb.add_field(name=f"💞 Partner :", value=f" {marLIst}💓",inline=False)
                await ctx.send(embed=emb)
                embed=discord.Embed(color=user.color,description=f"**❣ Siblings[{lensib}] :**\n{desc}")
                embed.set_author(name=f"{user.name}'s Siblings", icon_url=user.avatar_url)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(icon_url=self.bot.user.avatar_url)
                embed.set_image(url="https://giffiles.alphacoders.com/113/113317.gif")
                await ctx.send(embed=embed)
                return

def setup(bot):
    bot.add_cog(MarrySys(bot))
