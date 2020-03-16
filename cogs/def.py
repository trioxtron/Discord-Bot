import discord
from discord.ext import commands
import asyncio
import mysqllib


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass



    @commands.Cog.listener()
    async def on_member_join(self, member):
        commandsembed = discord.Embed(
            title = 'Commands',
            description = '''----------------
            -Rollen erstellen mit '!createrole [Rolle]' und '!addrole [Rolle]' sowie '!removerole [Rolle]' um sich eine Rolle zuzuweisen oder wegzunehmen

            -Platform hinzufügen/entfernen mit '!platform add [Plattform]' und '!platform remove [Plattform]'

            -'!pm @benutzer [Nachricht]' sendet dem Benutzer eine Private Nachricht über den Bot

            -'!coinflip'

            -'!joke'

            -'!pikachu'

            -'!ping'

            -'!pokemon' um dir ein Pokemon random auszugeben


            Kandycommands
            -------------
            -'!dsize'
            
            -'!kandykiss'

            -'!kandycouple'


            Minigames
            ---------
            -'!ssp' für Schere, Stein, Papier!

            -'!number' um eine Nummer zwischen 1 - 20 zu erraten

            -'!battle [User]' um gegen einen anderen User anzutreten

            ''',
            color = 1127128,
        )
        commandsembed.set_footer(text="Hier könnte Ihre Werbung stehen!")
        await member.send(embed=commandsembed)
        exc = mysqllib.exc
        exc.insert("fbn_coins", ["userid", "username", "coins"], [int(member.id), f"{member}", int(0)])


def setup(bot):
    bot.add_cog(Events(bot))