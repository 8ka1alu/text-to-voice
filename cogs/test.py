from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class test(commands.Cog):
    # testクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        ch = self.bot.get_channel(710092479151734795)
        m=0
        for p in message.attachments:
            m+=1
            await p.save(f"{m}.png")
        m=0
        for b in message.attachments:
            m+=1
            await ch.send(file=discord.File(f"{m}.png"),f"{ctx.guild.name},{ctx.channel.name}{ctx.author.name}")
            
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(test(bot)) 
# mainにBotを渡してインスタンス化し、Botにコグとして登録する。
