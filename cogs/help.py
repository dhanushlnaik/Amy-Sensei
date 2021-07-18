from os import name
import discord
from discord.ext import commands
from random import *
from db import check_prefix
Thugesh = 725612078764785694 # Main Server

# __COLORS__
color1 = discord.Color.from_rgb(93,71,82)
color2 = discord.Color.from_rgb(248,238,229)
color3 = discord.Color.from_rgb(228,188,148)
color4 = discord.Color.from_rgb(129,110,112)

randcol = [color1, color2, color3, color4]
melon = choice(randcol)

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, cog:str=None):
        lst = []
        if cog is None:
            helpEmbedall = discord.Embed(color=ctx.author.color, description=f"These Are the Available Commands For {self.bot.user.name}\nBot's Global Prefix Is - `amy `\nServer Prefix Is - `{check_prefix(ctx.guild.id)}`")
            helpEmbedall.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedall.set_thumbnail(url=ctx.author.avatar_url)
    
            helpEmbedall.add_field(name="__Fun__ [18]", value=f"`cat` `dog` `imgur` `gif` `marry` `div` `sib` `poke` `tellme` `rps` `random` `truth` `dare` `drunkify` `gay` `ship` `disown` `urban`", inline=False)
            helpEmbedall.add_field(name="__Misc__ [8]", value=f"`botstats` `ping` `prefix` `say` `pre` `owo` `avatar` `whois`", inline=False)
            helpEmbedall.add_field(name="__ToDo__ [3]", value=f"`setup_todo` `remove_todo` `todo`", inline=False)
            helpEmbedall.add_field(name="__Support__ [3]",value=f"`server` `github` `invite`" )
            await ctx.channel.send(embed=helpEmbedall)

        elif cog.lower() == '3' or cog.lower()=="todo":
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Todo functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 3 of 4")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] setup_todo <#channel>` - Set Server's Todo Channel \n`[2] remove_todo` - Disables Todo Functionality\n`[3] todo task1;task2;task3` - Make your interactive Todo List!", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        
        elif cog.lower() == '1' or cog.lower()=="fun":
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Fun functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 1 of 4")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] cat` - Random Cats! \n`[2] dog` - Random Dogs!\n`[3] imgur <search>` - Search for an image from imgur.\n`[4] gif <search>` - Search for an GIF. \n`[5] marry <member>` - Marry Someone\n`[6] div` - Divorce\n`[7] sib <member>` - Make Someone your E-sibling!\n`[8] poke <member>` - Poke Someone!\n`[9] tellme <statement>` - I'll tell if your statement is True or not!!\n`[10] rps` - Rock , Paper , Scissor!\n`[11] random <r/reddit>` - Random Reddit Post!\n`[12] truth` - Truth Question\n`[13] dare` - Dare Question!\n`[14] drunkify <text>` - Drunkify Some Random Text\n`[15] gay <user>` - UMM ! Very Mature Command XD\n`[16] ship <user1><user2>` - Ahem\n`[17] disown <user>` - Disown someone who is your Sibling.\n`[18] urban <word>` - Find Defination of a word.", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() in ['misc', 'miscellaneous', 'other','2']:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Miscellaneous functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 2 of 4")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] botstats`  - Show Bot Stats!\n`[2] ping` - Checkout whether bot is online.\n`[3] prefix` - Returns prefix of the bot.\n`[4] say [msg]` - Make bot say something!\n`[5] pre <newprefix>` - Change Prefix of the bot.\n`[6] owo [msg]` - Any Message to owo\n`[7] avatar <user>` - Shows Avatar of a User.\n`[8] whois <user>` - Shows User Info", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() == "support"or cog.lower() == "4":
            helpEmbedcog = discord.Embed(color=ctx.author.color, description=f'**Developer - <@{624174437821972480}>**')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 5 of 5")
            helpEmbedcog.add_field(name="Commands :",value=f"`[1] server` - Support Server Link\n`[2] github` - Gives Github Repository link.\n`[3] invite` - Invite Me in your server." )
            helpEmbedcog.add_field(name="DEV Links :", value=f"[Github](https://github.com/dhanushlnaik)\n[Instagram](https://instagram.com/dhanushlnaik)\n[Twitter](https://twitter.com/Dhanushlnaik)\n[buymeacoffee](https://www.buymeacoffee.com/dhanushlnaik)\n[Reddit](https://reddit.com/u/dhanushlnaik)\n[Support Server](https://discord.gg/dSxXksXg)", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        else: 
            await ctx.reply(f"That Command / Command Type Isn't there!")
            return
            


def setup(bot):
    bot.add_cog(Help(bot))
