import discord
from discord.ext import commands
import asyncio

class Platform(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def owner(self, ctx):
        return ctx.author.id == 302081657375293440

    platforms = {
        'pc': 528743677431119894,
        'ps': 528907130174963742,
        'switch': 530053813550317568,
        'pubg': 538654840927158303,
        'overwatch': 538656101579882496,
        'ow': 538656101579882496,
        'rocket league': 538656658339921922,
        'rl': 538656658339921922,
        'rocketleague': 538656658339921922,
    }

    @commands.group(pass_context=True, invoke_without_command=True, aliases=['plattform'])
    @commands.guild_only()
    async def platform(self, ctx):
        '''Mit `!platform add pc` oder `!platform remove pc` eine Gruppe hinzufügen oder entfernen '''

    @platform.command(pass_context=True)
    @commands.guild_only()
    async def add(self, ctx, platform):
        platform = platform.lower()
        if platform in self.platforms.keys():
            await ctx.author.add_roles(discord.Object(self.platforms[platform]))
            await ctx.message.delete()
        else:
            await ctx.send(f'Plattformen: {", ".join(self.platforms)}')

    @platform.command(pass_context=True)
    @commands.guild_only()
    async def remove(self, ctx, platform):
        platform = platform.lower()
        if platform in self.platforms.keys():
            await ctx.author.remove_roles(discord.Object(self.platforms[platform]))
            await ctx.message.delete()
        else:
            await ctx.send(f'Plattformen: {", ".join(self.platforms)}')

    @commands.command()
    async def createrole(self, ctx, *, text : str):
        reactions = ['✅', '❌']
        message = await ctx.send('Rolle {} soll wirklich erstellt werden?'.format(text))
        noah = self.bot.get_user(302081657375293440)
        for x in reactions:
            await message.add_reaction(x)
        try:
            hello = await self.bot.wait_for('reaction_add', timeout=15.0, check=lambda reaction, user: user == ctx.author)
        except asyncio.TimeoutError:
            return await ctx.send("Zu spät.")
        else:
            if str(hello[0]) == '✅':
                await ctx.send('Ok, angenommen.')
                nachricht = await  noah.send('Neue Rollenanfrage von {}. Rollenname: {}'.format(ctx.author, text))
                for y in reactions:
                    await nachricht.add_reaction(y)
                try:
                    hello2 = await self.bot.wait_for('reaction_add', timeout=15.0, check=lambda reaction, user: user == noah)
                except asyncio.TimeoutError:
                    return await noah.send("Zu spät.")
                else:
                    if str(hello2[0]) == '✅':
                        await noah.send('Rolle wird erstellt.')
                        guild = ctx.guild
                        newrole = await guild.create_role(name=text, colour=discord.Colour.light_grey())
                        user = ctx.author
                        await user.add_roles(newrole)
                        await ctx.send('Deine Rolle wurde erstellt und du hast sie bekommen')
                    elif str(hello2[0]) == '❌':
                        await noah.send('Ok, wird dem ersteller mitgeteilt.')
                        await ctx.send('Schade, deine Rollenanfrage wurde abgelehnt.')
                    else:
                        await noah.send('Fast.')
            elif str(hello[0]) == '❌':
                await ctx.send('Ok, dann nicht...')
            else:
                await ctx.send('Falscher Emoji.')

    @commands.command()
    async def addrole(self, ctx, *, roletext : discord.Role):
        if roletext.colour == discord.Colour.light_grey():
            user = ctx.author
            await user.add_roles(roletext)
            await ctx.send('Ok, du hast die Rolle bekommen.')
        else:
            await ctx.send('Diese Rolle kannst du nich haben.')

    @commands.command()
    async def removerole(self, ctx, *, roletext : discord.Role):
        if roletext.colour == discord.Colour.light_grey():
            user = ctx.author
            await user.remove_roles(roletext)
            await ctx.send('Ok, die Rolle wurde dir abgenommen.')
        else:
            await ctx.send('Diese Rolle gibts es nicht oder du hast sie nicht.')


    @commands.check(owner)
    @commands.command()
    async def giverole(self, ctx, typ : discord.Member, *, roletext : discord.Role):
        await typ.add_roles(roletext)
        await ctx.message.delete()

    @commands.check(owner)
    @commands.command()
    async def takerole(self, ctx, typ : discord.Member, *, roletext : discord.Role):
        await typ.remove_roles(roletext)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Platform(bot))