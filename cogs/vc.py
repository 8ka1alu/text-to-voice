import discord
from discord.ext import commands
import os
import r
from gtts import gTTS

conn = r.connect()

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

class VC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["connect","summon","con"])
    async def join(self, ctx):
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
        if message.author.bot:
            return
        vch = conn.exists('voice_ch')
        if vch == 0:
            await message.channel.send("-2")
            return
        ch_id = conn.get('voice_ch')
        await message.channel.send("-1")
        if message.channel.id == str(ch_id):
            voice_client = ctx.message.guild.voice_client
            myText = message.content
            language ='ja'
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("voice.mp3")
            await message.channel.send("1")
            ffmpeg_audio_source = discord.FFmpegPCMAudio("voice.mp3", **ffmpegopts)
            voice_client.play(ffmpeg_audio_source)
            await message.channel.send("2")
            return
                
def setup(bot):
    bot.add_cog(VC(bot))
