from discord.ext import commands
import discord
import json
import aiohttp
import random
from imgurpython import ImgurClient
from utils import PAT_GIFS, HUG_GIFS
import giphy_client
from giphy_client.rest import ApiException

tenor_key = ''
api_key = 'giphyApi Key'
imgur = ImgurClient('Client ID','Client Secret')

class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Working On it
    @commands.command()
    async def pat(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            gifg = random.choice(PAT_GIFS)
            emb = discord.Embed(color=ctx.author.color)
            emb.set_author(name=f"Thanks for the Pat QT!", icon_url=ctx.author.avatar_url)
            emb.set_image(url="https://i.imgur.com/fs0iKsZ.gif")
            await ctx.channel.send(embed=emb)
        else:
            try:
                gifg = random.choice(PAT_GIFS)
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} pats {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gifg)
                await ctx.channel.send(embed=emb)
            except:
                return

    @commands.command()
    async def hug(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            gifg = random.choice(HUG_GIFS)
            emb = discord.Embed(color=ctx.author.color)
            emb.set_author(name=f"Thanks for the Hug <33!", icon_url=ctx.author.avatar_url)
            emb.set_image(url=gifg)
            await ctx.channel.send(embed=emb)
        else:
            try:
                gifg = random.choice(HUG_GIFS)
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} hugs {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gifg)
                await ctx.channel.send(embed=emb)
            except:
                return
                
            
                
            
  
def setup(bot):
    bot.add_cog(Action(bot))