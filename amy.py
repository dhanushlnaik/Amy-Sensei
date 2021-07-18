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

melon = discord.Color.from_rgb(105, 84, 93)

# Load Bot Token from Environment Variable File(.env)
# env = environ.Env()
# env.read_env()
BOT_TOKEN = ''
DEFAULT_PREFIX = "amy "
def user_is_me(ctx):
    return ctx.message.author.id == 624174437821972480 #devID

async def prefix_get(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(DEFAULT_PREFIX)(bot, message)
    prefix = check_prefix(message.guild.id)
    return commands.when_mentioned_or(prefix)(bot, message)

# Bot Variables
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= prefix_get , case_insensitive=True, intents=intents)
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
    statuses = ["Actually Stalking brr", "Tatsuya <3", f"{len(bot.guilds)} servers !", "Suboi Mofo", "Kakarot", "Wolfey :O", "My Friends Suffer ! hehe", "K-Drama (Checkmate Weebs)"]
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


@bot.command(aliases=["pre"])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, newprefix:str):
    add_prefix(ctx.guild.id, newprefix )
    await ctx.reply("Done")

@bot.command()
@commands.check(user_is_me)
async def servername(ctx):
    activeservers = bot.guilds
    desc=""
    for guild in activeservers:
        desc = desc +","+ guild.name
    await ctx.send(desc)

@bot.command()
async def prefix(ctx):
    await message.channel.send(f"My prefix is  `{check_prefix(ctx.guild.id)}`")

@bot.event
async def on_message(message):
    

    love_words=["i love you amy","love you amy","amy i love you","amy is love"]


    emb = discord.Embed(title="", description=f"Thanks for loving me {message.author.mention}! UwU ", color=melon)
    
    emb.set_image(url="https://cdn.discordapp.com/attachments/859461880300568667/865548275766263838/703127469322010645.png")
  

    if message.content.lower() in love_words:
        if message.author.id == 624174437821972480:
            await message.reply(f"Same here😳")
            await message.add_reaction('<:amyChibiILY:863681666673147914>')
        else: 
            await message.channel.send(embed=emb)
            await message.add_reaction('<:amyChibiILY:863681666673147914>')
    await bot.process_commands(message)

async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Error!!!", description=f"Command not found.", color=ctx.author.color) 
        await ctx.send(embed=em)
    print(error)

bot.loop.create_task(switchpresence())
bot.run(BOT_TOKEN)
