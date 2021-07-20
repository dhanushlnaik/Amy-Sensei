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

