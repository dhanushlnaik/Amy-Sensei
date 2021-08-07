from os import name
import discord
from discord.ext import commands
from random import *
from db import check_prefix
Thugesh = 725612078764785694

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
        if cog is None:
            helpEmbedall = discord.Embed(color=ctx.author.color, description=f"These Are the Available Commands For {self.bot.user.name}\nBot's Global Prefix Is - `amy `\nServer Prefix Is - `{check_prefix(ctx.guild.id)}`")
            helpEmbedall.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedall.set_thumbnail(url=ctx.author.avatar_url)
            if ctx.guild.id == Thugesh:
                helpEmbedall.add_field(name="__Study__ [3]", value=f"`stats` `leaderboard` `doubtadd`", inline=False)
            helpEmbedall.add_field(name="__Fun__ [24]", value=f"`cat` `dog` `imgur` `gif` `marry` `div` `sib` `poke` `tellme` `rps` `random` `truth` `dare` `drunkify` `gay` `ship` `disown` `urban` `family` `joke` `insult` `quote` `nhie` `wyr`", inline=False)
            helpEmbedall.add_field(name="__Actions__ [9]", value=f"`pat` `hug` `kiss` `bite` `slap` `handhold` `tickle` `bully` `kill` `nom` `cuddle` `wave` `greet` `punch`", inline=False)
            helpEmbedall.add_field(name="__Misc__ [8]", value=f"`botstats` `ping` `prefix` `say` `pre` `owo` `avatar` `whois` `upvote`", inline=False)
            helpEmbedall.add_field(name="__ToDo__ [3]", value=f"`setup_todo` `remove_todo` `todo`", inline=False)
            helpEmbedall.add_field(name="__Support__ [3]",value=f"`server` `github` `invite`" )
            await ctx.channel.send(embed=helpEmbedall)
            return
        if cog.lower() == 'study' and ctx.guild.id == Thugesh:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Study functionality. [Thugesh Only]*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] stats <user>` - Shows Users Study Stats. \n`[2] leaderboard [d | w | m | total | doubts] ` - Checkout Server's Study Leaderboard.\n`[3] doubtadd <user> [points in integer]` - Add Doubt Points [Admin Only] ", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() in ["4", "todo", "setup_todo", "remove_todo"]:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Todo functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 4 of 5")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] setup_todo <#channel>` - Set Server's Todo Channel \n`[2] remove_todo` - Disables Todo Functionality\n`[3] todo task1;task2;task3` - Make your interactive Todo List!", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() in ["2", "pat", "action", "hug","kiss","slap","handhold","tickle","bully","kill","bite","nom", "cuddle", "wave", "greet", "punch"]:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Todo functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 2 of 5")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] pat <user>` - Pat Someone \n`[2] hug <user>` - Hug Someone \n`[3] kiss <user>` - Kiss Someone \n`[4] slap <user>` - Slap Someone \n`[5] handhold <user>` - Handhold Someone \n`[6] tickle <user>` - Tickle Someone \n`[7] bully <user>` - Bully Someone \n`[8] kill <user>` - Kill Someone \n`[9] bite <user>` - Bite Someone \n`[10] nom <user>` - Nom on Someone \n`[11] cuddle <user>` - Cuddle Someone \n`[12] wave <user>` - Wave Someone \n`[13] greet <user>` - Greet Someone \n`[14] punch <user>` - Punch Someone \n", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        
        elif cog.lower() in ["1", "fun", "cat","dog","imgur","gif","marry","div","sib","poke","tellme","rps","random","truth","dare","drunkify","gay","ship","disown","urban","family"]:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Fun functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 1 of 5")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] cat` - Random Cats! \n`[2] dog` - Random Dogs!\n`[3] imgur <search>` - Search for an image from imgur.\n`[4] gif <search>` - Search for an GIF. \n`[5] marry <member>` - Marry Someone\n`[6] div` - Divorce\n`[7] sib <member>` - Make Someone your E-sibling!\n`[8] poke <member>` - Poke Someone!\n`[9] tellme <statement>` - I'll tell if your statement is True or not!!\n`[10] rps` - Rock , Paper , Scissor!\n`[11] random <r/reddit>` - Random Reddit Post!\n`[12] truth` - Truth Question\n`[13] dare` - Dare Question!\n`[14] drunkify <text>` - Drunkify Some Random Text\n`[15] gay <user>` - UMM ! Very Mature Command XD\n`[16] ship <user1><user2>` - Ahem\n`[17] disown <user>` - Disown someone who is your Sibling.\n`[18] urban <word>` - Find Defination of a word.\n`[19] family <user>` - Find Family Tree of a User.\n`[20] joke` - Random Joke\n`[21] quote` - Random Quote.\n`[22] nhie` - Never have I Ever.\n`[23] wyr` - Would You Rather.\n`[24] insult @user` - Insults A User.", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() in ['misc', 'miscellaneous', 'other','3']:
            helpEmbedcog = discord.Embed(color=ctx.author.color, description='*Commands directly related to Miscellaneous functionality.*')
            helpEmbedcog.set_author(name="Amy Sensei - Help", icon_url=self.bot.user.avatar_url)
            helpEmbedcog.set_thumbnail(url=ctx.author.avatar_url)
            helpEmbedcog.set_footer(text=f"Page 3 of 5")
            helpEmbedcog.add_field(name="Commands :", value=f"`[1] botstats`  - Show Bot Stats!\n`[2] ping` - Checkout whether bot is online.\n`[3] prefix` - Returns prefix of the bot.\n`[4] say [msg]` - Make bot say something!\n`[5] pre <newprefix>` - Change Prefix of the bot.\n`[6] owo [msg]` - Any Message to owo\n`[7] avatar <user>` - Shows Avatar of a User.\n`[8] whois <user>` - Shows User Info\n`[9] upvote`  - Returns Upvote Link!", inline=False)
            await ctx.channel.send(embed=helpEmbedcog)
            return
        elif cog.lower() == "support"or cog.lower() == "5":
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
