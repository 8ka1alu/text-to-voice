import discord
from discord.ext import commands
import os
import r
from gtts import gTTS
import discordbot as dib

prefix = dib.prefix

conn = r.connect()

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

class DIC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["connect","summon","con"])
    async def join(self, ctx):
        """ボイスチャンネルに接続"""
        voice_state = ctx.author.voice

        if (not voice_state) or (not voice_state.channel):
            await ctx.send("先にボイスチャンネルに入っている必要があります。")
            return

        vch = conn.exists('voice_ch')
        if vch == 1:
            ch_id = conn.get('voice_ch')
            await ctx.send(f"現在別チャンネルにて使用中です(id:{ch_id})")
            return

        channel = voice_state.channel

        await channel.connect()

        conn.set('voice_ch',ctx.channel.id)

        embed = discord.Embed(title="**接続完了**", description=f"接続チャンネル名```{channel.name}```")
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed = embed)

    @commands.command(aliases=["disconnect","bye","dis"])
    async def leave(self, ctx):
        """ボイスチャンネルから退室"""
        voice_client = ctx.message.guild.voice_client

        if not voice_client:
            await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
            return

        await voice_client.disconnect()

        conn.delete('voice_ch')

        embed = discord.Embed(title="**ボイスチャンネルから切断しました**", description=None)
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        """メッセージの変換"""
        if message.author.bot:
            return

        if message.content.startswith(prefix):
            return

        vch = conn.exists('voice_ch')
        if vch == 0:
            return

        ch_id = conn.get('voice_ch')
        if str(message.channel.id) == ch_id:
            voice_client = message.guild.voice_client
            myText = message.content
            language ='ja'
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("voice.mp3")
            ffmpeg_audio_source = discord.FFmpegPCMAudio("voice.mp3", **ffmpegopts)
            voice_client.play(ffmpeg_audio_source)
            return
            
def setup(bot):
    bot.add_cog(DIC(bot))
