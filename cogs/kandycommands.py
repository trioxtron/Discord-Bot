import discord
from discord.ext import commands
import random
import asyncio

class kandycommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dsize(self, ctx):
        size = random.randint(0, 30)
        await ctx.send(f"{ctx.author.mention} `hat {size}cm`")

    @commands.command()
    async def kandycouple(self, ctx):
        couple = random.randint(0, 13)
        await ctx.send(f"`{couple}/10`")

    @commands.command()
    async def kandykiss(self, ctx):
        kiss = random.randint(0, 100)
        await ctx.send(f"`{kiss}%/100%`")

def setup(bot):
    bot.add_cog(kandycommands(bot))
