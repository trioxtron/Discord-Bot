import discord
from discord.ext import commands
import asyncio


class Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.users = []
        self.channel = []


    @commands.command()
    async def newchannel(self, ctx, serie : str):
        beta = self.bot.get_channel(576384240749379594)
        cate = beta.category
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                    ctx.message.author: discord.PermissionOverwrite(read_messages=True),
                    }
        reactions = ['✅', '❌']
        owner = self.bot.get_user(302081657375293440)
        guild = ctx.message.guild
        message = await owner.send("Soll der Channel erstellt werden?")
        seriesembed = discord.Embed(
            title = f'Diskussion über die Serie: {serie}',
            description = 'Drücke auf das Bereits vorgegebene Emote um den Channel zu sehen',
            color = discord.Color.gold()
        )


        for reaction in reactions:
            await message.add_reaction(reaction)

        try:
            hello = await self.bot.wait_for('reaction_add', timeout=600.0, check=lambda reaction, user: user == owner)

        except asyncio.TimeoutError:
            pass

        else:
            if str(hello[0]) == '✅':
                await owner.send('Ok, Channel wird erstellt')

                createchannel = await guild.create_text_channel(name=serie, overwrites=overwrites)
                await createchannel.edit(category=cate)

                accesmessage = await ctx.send(embed=seriesembed)

                self.channel.append(accesmessage.id)

                await accesmessage.add_reaction('✅')


            elif str(hello[0]) == '❌':
                pass


def setup(bot):
    bot.add_cog(Channel(bot))