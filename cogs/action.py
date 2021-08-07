from discord.ext import commands
import discord
import random


num = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
num2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]


class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pat(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            emb = discord.Embed(color=ctx.author.color)
            emb.set_author(name=f"Thanks for the Pat QT!", icon_url=ctx.author.avatar_url)
            emb.set_image(url="https://i.imgur.com/fs0iKsZ.gif")
            await ctx.channel.send(embed=emb)
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/Pat%20Gifs%2Fpat{x}.gif?alt=media&token=16445a16-8c31-4e05-ba09-112d1cc929e5"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} pats {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return

    @commands.command()
    async def hug(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/hug%20gifs%2Fpat{x}.gif?alt=media&token=012befd5-7d3f-4221-9691-b9934b02da58"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} hugs {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command()
    async def kiss(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/kiss%20gifs%2Fkiss{x}.gif?alt=media&token=b421bf85-2894-4e6e-8301-827e492cdb4b"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} kisses {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command()
    async def bite(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/bite%2Fbite{x}.gif?alt=media&token=3a59bd3a-f1e1-4a93-9722-ec456d91e21c"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} bites {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command()
    async def slap(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/slap%2Fslap{x}.gif?alt=media&token=551eac15-4a9a-4cec-a827-e3b7d21c6462"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} slaps {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command(aliases=['hh', 'hand', 'hands'])
    async def handhold(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/handhold%2Fhandhold{x}.gif?alt=media&token=c3862ff4-e7f0-4c07-8d8a-90c199da2a8d"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} holds {user.name}'s hands~ adorable!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command()
    async def tickle(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/tickle%2Ftickle{x}.gif?alt=media&token=e94b0335-1ff0-4a6d-8d99-6766179589e1"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} tickles {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return              
    @commands.command()
    async def bully(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/bully%2Fbully{x}.gif?alt=media&token=b1a14c6a-d6cf-49da-b4bf-29172655e547"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} bullies {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
    @commands.command()
    async def kill(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num2)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/kill%2Fkill{x}.gif?alt=media&token=112b3a8b-a10a-4e3b-840e-3e5120e02d63"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} kills {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return           

    @commands.command()
    async def nom(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/bite%2Fbite{x}.gif?alt=media&token=3a59bd3a-f1e1-4a93-9722-ec456d91e21c"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} noms on {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return   

    @commands.command()
    async def cuddle(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/cuddle%2Fcuddle{x}.gif?alt=media&token=21be9a7a-0a66-454f-b3c3-bd073f9f39cf"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} cuddles {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
                
    @commands.command()
    async def wave(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/greet%2Fgreet{x}.gif?alt=media&token=40bf1292-cf17-4836-8e70-a44748ca4f0c"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} waves at {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return

    @commands.command()
    async def greet(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/greet%2Fgreet{x}.gif?alt=media&token=40bf1292-cf17-4836-8e70-a44748ca4f0c"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} greets {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return

    @commands.command()
    async def punch(self, ctx, user:discord.Member=None):
        if user is None or user.id == self.bot.user.id:
            await ctx.channel.send(f"🚫 {ctx.author.mention}, Please Mention a User.")
        else:
            try:
                x = random.choice(num)
                gif_url=f"https://firebasestorage.googleapis.com/v0/b/aiko-mizuki.appspot.com/o/punch%2Fpunch{x}.gif?alt=media&token=a0372b4d-7e8e-4268-a855-0f41a7833337"
                emb = discord.Embed(color=ctx.author.color)
                emb.set_author(name=f"{ctx.author.name} punches {user.name}!", icon_url=ctx.author.avatar_url)
                emb.set_image(url=gif_url)
                await ctx.channel.send(embed=emb)
            except:
                return
  
def setup(bot):
    bot.add_cog(Action(bot))
