import discord 
import os

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

discord_voice_channel_id = '607543283320881161' # 特定のボイスチャンネルを指定
youtube_url = 'https://www.youtube.com/watch?v=mN7u3h-BZjY' # youtubeのURLを指定

voice = None
player = None

#起動メッセージ
@client.event
async def on_ready():
    print('Hello World,リマインドbotプログラム「project-youtube」、起動しました')

@client.event
async def on_message(message):
    global voice, player
    msg = message.content
    if message.author.bot:
        return
    
    if msg == '!play':
        if message.author.voice_channel is None:
            await client.send_message(message.channel ,'ボイスチャンネルに参加してからコマンドを打ってください。')
            return
        if voice == None:
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                voice = await client.join_voice_channel(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                voice = await client.join_voice_channel(client.get_channel(discord_voice_channel_id))
        # 接続済みか確認
        elif(voice.is_connected() == True):
            # 再生中の場合は一度停止
            if(player.is_playing()):
                player.stop()
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                await voice.move_to(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                await voice.move_to(client.get_channel(discord_voice_channel_id))
        # youtubeからダウンロードし、再生
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
        return
    
    # 再生中の音楽を停止させる
    if msg == '!stop':
        if(player.is_playing()):
                player.stop()
                return
    
    # botをボイスチャットから切断させる
    if msg == '!disconnect':
        if voice is not None:
            await voice.disconnect()
            voice = None
            return


client.run(TOKEN)
