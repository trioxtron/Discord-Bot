import discord
from discord.ext import commands
import asyncio
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ssp(self, ctx):
        variables = [
        "Schere",
        "Stein",
        "Papier",
        ]
        await ctx.send("Schere, Stein, Papier!")
        choice = random.choice(variables)
        try:   
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15.0)
            if  choice == variables[0] and msg.content == "Schere":
                await ctx.send("Wir haben das selbe. Nochmal.")
            elif  choice == variables[0] and msg.content == "Stein":
                await ctx.send(f"Du gewinnst, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[0] and msg.content == "Papier":
                await ctx.send(f"Ich gewinne, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[1] and msg.content == "Schere":
                await ctx.send(f"Ich gewinne, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[1] and msg.content == "Stein":
                await ctx.send("Wir haben das selbe. Nochmal.")
            elif  choice == variables[1] and msg.content == "Papier":
                await ctx.send(f"Du gewinnst, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[2] and msg.content == "Schere":
                await ctx.send(f"Du gewinnst, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[2] and msg.content == "Stein": 
                await ctx.send(f"Ich gewinne, ich hatte {choice} und du {msg.content}")
            elif  choice == variables[2] and msg.content == "Papier":
                await ctx.send("Wir haben das selbe. Nochmal.")
            else:
                pass
        except asyncio.TimeoutError:
            return await ctx.send('Du warst zu spät')
        else:
            pass

    @commands.command()
    async def number(self, ctx):
        await ctx.send('Schätze eine Nummer zwischen 1 und 20')
        thenumber = random.randint(1, 20)
        try:   
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15.0)
            if int(msg.content) == thenumber:
                await ctx.send(f" Die Antwort ist {(thenumber)}, du hast {int(msg.content)} gesagt und somit gewonnen") 
            else:
                await ctx.send(f" Die Antwort ist {(thenumber)}, du hast {msg.content} gesagt und somit verloren") 
        except asyncio.TimeoutError:
            return await ctx.send('Du warst zu spät')
        else:
            pass

    @commands.command()
    async def battle(self, ctx, typ : discord.Member):
        typ1 = typ.mention
        typ2 = ctx.author.mention
        batteling = [typ1, typ2]
        winner = random.choice(batteling)
        await ctx.send(f"{winner} gewinnt.")

    @commands.command()
    async def sspagainst(self, ctx, typ : discord.Member):
        typ1 = typ.mention
        typ2 = ctx.author.mention        
        await ctx.send(f"{typ2} will Schere, Stein, Papier gegen dich spielen {typ1} in...")
        await asyncio.sleep(1)
        await ctx.send("3")
        await asyncio.sleep(1)
        await ctx.send("2")
        await asyncio.sleep(1)
        await ctx.send("1")



def setup(bot):
    bot.add_cog(Games(bot))
