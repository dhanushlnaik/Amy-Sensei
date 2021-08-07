import os
import discord
from discord.ext import commands
import traceback
import environ
from db import *
import random
import asyncio
from discord_components import *
from random import choice

owners=[710852927543050292, 614784461430587413, 624174437821972480, 826073652440858634]

melon = discord.Color.from_rgb(105, 84, 93)

# Load Bot Token from Environment Variable File(.env)
env = environ.Env()
env.read_env()
BOT_TOKEN = env.read_env('BOT_TOKEN')
DEFAULT_PREFIX = "amy "
def user_is_me(ctx):
    return ctx.message.author.id in owners

async def prefix_get(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(DEFAULT_PREFIX)(bot, message)
    prefix = check_prefix(message.guild.id)
    return commands.when_mentioned_or(prefix)(bot, message)

# Bot Variables
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= prefix_get , case_insensitive=True, intents=intents, owner_id=set(owners))
bot.remove_command("help")

# Load & Unload Cog Functions
def unload_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            try:
                bot.unload_extension(f"cogs.{file[:-3]}")
            except Exception as e:
                print(f"COG UNLOAD ERROR : {e}")


def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            try:
                bot.load_extension(f"cogs.{file[:-3]}")
                print(f'Loaded cog: {file[:-3]}'.title())
            except Exception as e:
                print(f"COG LOAD ERROR : {e}\n\n{traceback.format_exc()}\n\n")


@bot.command(aliases=["reload"])
@commands.check(user_is_me)
async def reloadcogs(ctx):
    unload_cogs()
    load_cogs()
    await ctx.reply("All Cogs Reloaded!")

async def switchpresence():
    await bot.wait_until_ready()
    statuses = ["Actually Stalking brr", "Tatsuya <3", f"{len(bot.guilds)} servers !", "Suboi Mofo", "Kakarot", "Wolfey :O", "My Friends Suffer ! hehe", "K-Drama (Checkmate Weebs)", "FEENITE BHAIYA"]
    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print(f"Logged in as : {bot.user.name} \n ID : {bot.user.id}")
    print(f"Total Servers : {len(bot.guilds)}\n")
    DiscordComponents(bot)

    load_cogs()
    print("BOT is awake\n")


@bot.command()                                                                                                                                            
@commands.check(user_is_me)
async def servername(ctx):
    activeservers = bot.guilds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    desc=""
    n=0
    for guild in activeservers:
        n +=1
        desc += f"[{n}] {guild.name}\n"
    await ctx.send(f"`{desc}`")
   
@bot.command(aliases=["pre","setprefix"])
async def prefix(ctx, newpre:str=None):
    if newpre is None:
        await ctx.channel.send(f"My prefix is  `{check_prefix(ctx.guild.id)}`")
        return
    else: 
        if ctx.message.author.server_permission.administrator:
            add_prefix(ctx.guild.id, newpre)
            await ctx.reply(f"New Prefix :  `{check_prefix(ctx.guild.id)}` ")
            return
        else:
            await ctx.reply(f"You are not an Admin!")
            return


@bot.event
async def on_message(message):
    if str(message.content.lower()) == "69":
        await message.reply("*Ahem!*")
        return

    love_words=["i love you amy","love you amy","amy i love you","amy is love"]
    hate_words = ["i hate you amy","hate you amy","amy i hate you","amy is noob", "amy cancer"]


    emb = discord.Embed(title="", description=f"Thanks for loving me {message.author.mention}! UwU ", color=melon)
    
    emb.set_image(url="https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/amy%20sensei%2Floveroll.gif?alt=media&token=e7cf8f48-bc97-4357-8840-e70f313457bb")
  
    loveAmy = any(word in message.content.lower() for word in love_words )
    hateAmy = any(word in message.content.lower() for word in hate_words )
    if  loveAmy:
        if message.author.id == 624174437821972480:
            await message.reply(f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/amy%20sensei%2Fily2.gif?alt=media&token=a155e8db-7839-44d6-80e5-14160fabe6cf")
            await message.add_reaction('<:amyChibiILY:863681666673147914>')
        else: 
            await message.channel.send(embed=emb)
            await message.add_reaction('<:amyChibiILY:863681666673147914>')
    elif hateAmy:
        await message.reply("https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/amy%20sensei%2Fcry2.gif?alt=media&token=c0f7e3f6-a9e2-4412-bdfb-7d0dab50951b")
        await message.add_reaction('<:amyBed:863681197577601024>')
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Error!!!", description=f"Command not found.", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    elif isinstance(error, commands.MissingPermissions): 
        em = discord.Embed(title=f"Error!!!", description=f"You are missing the required permissions to run this command!", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    elif isinstance(error, commands.MissingRequiredArgument): 
        em = discord.Embed(title=f"Error!!!", description=f"Missing a required argument: {error.param}", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        em = discord.Embed(title=f"Error!!!", description=f"{message}", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    elif isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Error!!!", description=f"Missing a required argument: {error.param}", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    elif isinstance(error, commands.ConversionError):
        message = str(error)
        em = discord.Embed(title=f"Error!!!", description=f"{message}", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)
    else:
        message = "Oh no! Something went wrong while running the command!"
        em = discord.Embed(title=f"Error!!!", description=f"{message}", color=ctx.author.color) 
        await ctx.send(embed=em)
        print(error)

bot.loop.create_task(switchpresence())
bot.run(BOT_TOKEN)
