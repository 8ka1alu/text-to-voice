import discord
from discord.ext import commands
import os


if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

class VC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["connect","summon","con"])
    async def join(self, ctx):
        voice_state = ctx.author.voice

        if (not voice_state) or (not voice_state.channel):
            await ctx.send("先にボイスチャンネルに入っている必要があります。")
            return

        channel = voice_state.channel

        await channel.connect()

        embed = discord.Embed(title="**接続完了**", description=f"接続チャンネル名```{channel.name}```")
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed = embed)

    @commands.command(aliases=["disconnect","bye","dis"])
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client

        if not voice_client:
            await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
            return

        await voice_client.disconnect()

        embed = discord.Embed(title="**ボイスチャンネルから切断しました**", description=None)
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_message(self, message):


def setup(bot):
    bot.add_cog(VC(bot))
