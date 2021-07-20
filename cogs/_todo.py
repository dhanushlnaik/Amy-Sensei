from discord import Embed , utils , Color, TextChannel
import datetime
from discord.ext import commands
import pyrebase
from json import loads , load 
from db import check_prefix

with open("firebase.json", "r") as read_file:
    firebase = pyrebase.initialize_app(load(read_file))
db = firebase.database()

def new_guild(guild_id: int):
    db.child("Guild_Var").child(guild_id).set(
        {"prefix":'amy ', "todochannel":0})

# Add todoChannel in Database
def add_todoChannel(guild_id: int, todoChannel: int):
    guild_todoChannel = db.child("Guild_Var").child(guild_id).get().val()
    if guild_todoChannel == None:
        new_guild(guild_id)
    guild_todoChannel["todochannel"] = todoChannel
    db.child("Guild_Var").child(guild_id).set(guild_todoChannel)

# Check todoChannel 
def check_todoChannel(guild_id: int):
    guild_todoChannel = db.child("Guild_Var").child(guild_id).get().val()
    if guild_todoChannel == None:
        new_guild(guild_id)
        guild_todoChannel = db.child("Guild_Var").child(guild_id).get().val()
    todoChannel = int(guild_todoChannel["todochannel"])
    return todoChannel

def rmv_todoChannel(guild_id: int):
    guild_todoChannel = db.child("Guild_Var").child(guild_id).get().val()
    if guild_todoChannel == None:
        new_guild(guild_id)
        guild_todoChannel = db.child("Guild_Var").child(guild_id).get().val()
    guild_todoChannel["todochannel"] = 0
    db.child("Guild_Var").child(guild_id).set(guild_todoChannel)

# Variables
nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣",
        "🔟", "🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮"] 
todoChannel = 0
green = Color.green()
red = Color.red()


class Todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup_todo(self,ctx, channel:TextChannel=None):
        try:
            if channel is None:
                await ctx.reply("Please Mention a Channel!")
                pass
            guild = int(ctx.guild.id)
            add_todoChannel(guild, channel.id)
            await ctx.reply(f"Added TODO channel : <#{channel.id}>")
        except Exception as e:
            print(e)

    @commands.command()
    async def remove_todo(self,ctx, channel:TextChannel=None):
        try:
            guild = int(ctx.guild.id)
            rmv_todoChannel(guild, channel.id)
            await ctx.reply(f"Removed TODO channel")
        except Exception as e:
            print(e)
    
    @commands.command()
    async def todo(self, ctx,*,message):
        todoChannel = check_todoChannel(ctx.guild.id)
        if todoChannel is 0:
            await ctx.reply('Please Setup the Todo Channel')
        elif todoChannel == ctx.channel.id:
            if ';' in message:
                tasks = message.replace(';', '/n').split('/n')

            else:
                tasks = message.split()
            n = len(tasks)
            
            embed = Embed(title="TO-DO", color=red, description=f"Assigned by - {ctx.author.mention}")
            for i in range(len(tasks)):
                embed.add_field(name=f"Task ({i+1}/{n})", value=f"<:notdone:864136119313235998> {tasks[i]}", inline=False)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=ctx.author.name)
            msg = await ctx.send(embed=embed)
            for i in range(n):
                await msg.add_reaction(nums[i])
        else:
            await ctx.reply(f"Works only in <#{todoChannel}>")

        
        

    @commands.Cog.listener()
    async def on_message(self, message):
        todoChannel = check_todoChannel(message.guild.id)
        if message.channel.id == todoChannel and not message.author.bot:
            await message.delete()


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        todoChannel = check_todoChannel(int(reaction.guild_id))
        if reaction.channel_id == todoChannel and not reaction.member.bot:
            channel_ = utils.get(self.bot.get_all_channels(), id=todoChannel)
            msg = await channel_.fetch_message(reaction.message_id)      
            embed = msg.embeds[0].to_dict()
            count = 0
            for x in embed:
                if isinstance(embed[x], list):
                    count += len(embed[x])
            userID_without = embed['description'].replace('Assigned by - <@','').replace('!', '').replace('>','')
            if str(reaction.user_id) == str(userID_without):
                
                embedN = Embed(title="TO-DO",color=green, description=f"Assigned by - <@{reaction.user_id}>")
                for m in range(count):

                    
                    i = nums.index(reaction.emoji.name)
                    
                    if m == i:
                        embedN.add_field(name=f"Task({m+1}/{count})", value=embed['fields'][m]['value'].replace('<:notdone:864136119313235998>','<:done:864136078695989258>'), inline=False)
                    else:
                        embedN.add_field(name=f"Task({m+1}/{count})", value=f"{embed['fields'][m]['value']}", inline=False)
                embedN.timestamp = datetime.datetime.utcnow()
                embedN.set_footer(text=embed['footer']['text'])    
                await msg.edit(embed=embedN)
            else:
                pass
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction):
        todoChannel = check_todoChannel(int(reaction.guild_id))
        if reaction.channel_id == todoChannel :
            channel_ = utils.get(self.bot.get_all_channels(), id=todoChannel)
            msg = await channel_.fetch_message(reaction.message_id)      
            embed = msg.embeds[0].to_dict()
            count = 0
            for x in embed:
                if isinstance(embed[x], list):
                    count += len(embed[x])
            userID_without = embed['description'].replace('Assigned by - <@','').replace('!', '').replace('>','')
            
            if str(reaction.user_id) == str(userID_without):
                
                embedN = Embed(title="TO-DO",color=red, description=f"Assigned by - <@{reaction.user_id}>")
                for m in range(count):

                    
                    i = nums.index(reaction.emoji.name)
                    
                    if m == i:
                        embedN.add_field(name=f"Task({m+1}/{count})", value=embed['fields'][m]['value'].replace('<:done:864136078695989258>','<:notdone:864136119313235998>'), inline=False)
                    else:
                        embedN.add_field(name=f"Task({m+1}/{count})", value=f"{embed['fields'][m]['value']}", inline=False)
                embedN.timestamp = datetime.datetime.utcnow()
                embedN.set_footer(text=embed['footer']['text'])    
                await msg.edit(embed=embedN)
            else:
                pass



def setup(bot):
    bot.add_cog(Todo(bot))