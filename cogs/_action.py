from discord.ext import commands
import discord
import json
import aiohttp
import random
from imgurpython import ImgurClient
from utils import PAT_GIFS
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
        if user is None:
            await ctx.send('**Please mention a user**')
        else:
            api_instance = giphy_client.DefaultApi()

            try:
                api_response = api_instance.gifs_search_get(api_key, "anime+pat", limit=5, rating='g')
                lst = list(api_response.data)
                rgiff = random.choice(lst)
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} pats {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=f"https://media.giphy.com/media/{rgiff.id}/giphy.gif")
                await ctx.channel.send(embed=emb)
            except ApiException as e:
                print("Exception when calling Api as "+e)
                
            
                
            # gifg = random.choice(PAT_GIFS)
            
def setup(bot):
    bot.add_cog(Action(bot))