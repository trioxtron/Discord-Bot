import discord
from discord.ext import commands
import asyncio
import youtube_dl


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    players = {}


    @commands.command()
    async def connect(self, ctx):
        channel = ctx.author.voice.channel
        await discord.VoiceChannel.connect(channel)


    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()


    @commands.command()
    async def play(self, ctx, url):
        guild = ctx.message.guild
        vc = guild.voice_client
        print(f"------------------------{guild.id}------------------------")
        player = await vc.create_ytdl_player(url)
        self.players[guild.id] = player
        player.start()


    @commands.command()
    async def pause(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send('I am not currently playing anything!', delete_after=20)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'{ctx.author} hat den Song pausiert')


    @commands.command()
    async def resume(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!', delete_after=20)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'{ctx.author} lässt den Song weiter spielen.')





def setup(bot):
    bot.add_cog(Music(bot))
