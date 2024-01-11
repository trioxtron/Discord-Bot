import discord
from discord.ext import commands
import random
import jokes
import asyncio
import time

bot = commands.Bot(command_prefix='!', description="", case_intensitive=True)

cogs = [  'kandycommands',
          'games',
          'channel',
          'def',
          'ttt',
          'role',
          'music',
          'movie',
          'wer_bietet_mehr',
          
        ]

for data in cogs:
    bot.load_extension(f'cogs.{data}')


async def owner(ctx):
    return ctx.author.id == 302081657375293440


@bot.command()
async def reload(ctx, ext : str):
    bot.reload_extension(f'cogs.{ext}')
    await ctx.send(f"reloaded ``{ext}`` succesfully")


@bot.command()
async def coinflip(ctx):
    variables = [
     'Zahl',
     'Kopf', 
    ]
    await ctx.send('Ich werfe die Münze. Wöfür bist du?')
    try:   
        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15.0)
        await ctx.send(f" Die Antwort ist {(random.choice(variables))}, du hast {msg.content} gesagt") 
    except asyncio.TimeoutError:
        return await ctx.send('Du warst zu spät')
    else:
        pass


@bot.command()
async def joke(ctx):
    jokeembed = discord.Embed(
        title = 'Joke',
        description = (random.choice(jokes.jokes)),
        color = random.randint(0, 0xFFFFFF)
    )  
    jokeembed.set_footer(text='Jokes from https://www.aberwitzig.com/')
    await ctx.send(embed=jokeembed)
    await ctx.message.delete()


@bot.command()
async def pm(ctx, typ: discord.Member, *, text : str):
    await ctx.message.delete()
    await typ.send(text)


@bot.command()
async def commandlist(ctx):
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
    await ctx.send(embed=commandsembed)


@bot.command()
async def clear(ctx, number=5):
    if ctx.author.id == 302081657375293440:
        channel = ctx.message.channel
        await ctx.message.delete()
        await channel.purge(limit=number)
    else:
        pass


@bot.command()
async def pikachu(ctx):
    await ctx.send('https://gyazo.com/c3ce0f4f7cbbc69bb4220130c53fcfb3')


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    latency = bot.latency 
    before = time.monotonic()
    message = await ctx.send("Warte einen Moment...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"{ctx.author.mention} hat `{int(ping)}ms` \nDer bot hat `{latency}`")


@bot.command()
async def pokemon(ctx):
    poke = ["https://gyazo.com/c3ce0f4f7cbbc69bb4220130c53fcfb3", "https://gyazo.com/e81ed30ab1e5abbfd46047f5b79a3091", "https://gyazo.com/ae21388e71f6b3b120b3ab48a57d4417", "https://gyazo.com/4c7922d6e87061fd56abca788f77c176", "https://gyazo.com/3ad8cebbf71fb5b41a418460b640743e", "https://gyazo.com/3c5ddefde898fadfc5f8a0f176d489a5", "https://gyazo.com/e0c177529ec3b48092c6be695e271668",]
    randompokemon = random.choice(poke)
    await ctx.send(randompokemon)


bot.run("DISCOR_BOT_TOKEN") 
