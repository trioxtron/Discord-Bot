import discord
from discord.ext import commands
import asyncio
import mysqllib

class Movies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def movieadd(self, ctx, platform_name = "noplatform", *, movie_name):                                     #Command to add a movie to the database 
        exc = mysqllib.exc

        await ctx.message.delete()

        exc.insert("movielist", ["moviename", "platformname"], [f"{movie_name}", f"{platform_name}"])               #Inserting the movie with the platform you can watch it
                                                     


    @commands.command()
    async def movielist(self, ctx, platform_name = "noplatform"):                                                   #Command to get a list of all movies on the watchlist on a specific platform
        exc = mysqllib.exc

        await ctx.message.delete()

        if platform_name == "everyplatform":
            movies = exc.get("movielist", ["moviename"], "None")

        else:
            movies = exc.get("movielist", ["moviename"], f"platformname = '{platform_name}'", "where")              #Getting the list of movies you can watch on a specific platform

        moviesmessage = ""

        for singlemovie in movies:                                                                                  #Splitting the tuple and letting it send just one message
            moviesmessage = moviesmessage + f"{singlemovie[0]} \n"

        movielistembed = discord.Embed(
            title = f'Movies you want to watch on {platform_name}',
            description = f'{moviesmessage}',
            color = discord.Color.gold(),

        )


        if moviesmessage == "":
            await ctx.send("There is no movie in the list you want to watch")

        else:
            await ctx.send(embed=movielistembed)



    @commands.command()
    async def moviedelete(self, ctx, *, movie_name):
        exc = mysqllib.exc

        await ctx.message.delete()

        exc.throw("movielist", [f"moviename = '{movie_name}'"])                                                      #Deleting a specific movie in the list



    @commands.command()
    async def movieplatform(self, ctx, *, movie_name):
        exc = mysqllib.exc

        await ctx.message.delete()

        platform = ""

        platform_name = exc.get("movielist", ["platformname"], f"moviename = '{movie_name}'", "where")              #Getting the name of the platform   

        for platforms in platform_name:
            platform = platform + f"{platforms[0]} \n"                                                              #Splitting the tuple and letting it send just one message


        platform_nameembed = discord.Embed(
            title = f'You can watch {movie_name} on',
            description = f"{platform}",
            color = discord.Color.gold(),

        )

        await ctx.send(embed=platform_nameembed)
    


    @commands.command()
    async def movieplatformupdate(self, ctx, newplatform, *, movie_name):
        exc = mysqllib.exc

        await ctx.message.delete()

        exc.update("movielist", [f"platformname = %s"], [f"{newplatform}"], "moviename", f"{movie_name}")        #Updating the platform of an specific movie



    @commands.command()
    async def moviehelp(self, ctx):

        moviehelpembed = discord.Embed(
            title = 'Alle Commands zum Thema Movies:',
            color = discord.Color.gold()
        )
        moviehelpembed.add_field(name="movieadd", value="Füge einen Film in die Datenbank hinzu und bestimme die Platform, auf er geschaut werden kann.\nFalls keine Platform:\n-> Platformname = noplatform\n\n!movieadd [Platformname] [Moviename]\n", inline=False)
        moviehelpembed.add_field(name="moviedelete", value="Lösche einen Film aus der Datenbank.\n\n!moviedelete [Moviename]\n", inline=False)
        moviehelpembed.add_field(name="movielist", value="Lasse eine Liste aller Filme ausgeben.\nFalls Platform egal ist oder keine spezielle gewünscht ist:\n->Platformname = everyplatform\n\n!movielist [Platformname]\n", inline=False)
        moviehelpembed.add_field(name="movieplatform", value="Lasse dir ausgeben, auf welcher Platform der Film derzeit geschaut werden kann.\n\n!movieplatform [Moviename]\n", inline=False)
        moviehelpembed.add_field(name="movieplatformupdate", value="Ändere die Platform auf der ein Film geschaut werden kann.\n\n!movieplatformupdate [Newplatform] [Moviename]\n", inline=False)

        await ctx.send(embed=moviehelpembed)





def setup(bot):
    bot.add_cog(Movies(bot))