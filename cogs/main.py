from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime
import r

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class main(commands.Cog):
    # mainクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        """オウム返し"""
        if ctx.author.id == great_owner_id:
            return
        await ctx.send(f'{what}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 159985870458322944: # MEE6からのメッセージかどうかを判別
            if message.content.startswith("!levelup"):
                level = int(message.content.split()[-2]) # メッセージを分解
                t_name = message.content.split()[-1] # メッセージを分解
                target = discord.utils.get(message.server.members, mention=t_name) # レベルアップしたユーザーのIDを取得
                levels = 10 - str(level)
                replys = f"{t_name}さん、が{str(level)}レベルになりました。\nあと{levels}で上級市民になります。" # レベルアップメッセージ
                await self.bot.get_channel(695795193244286997).send(replys)

                if level == 10: # レベル1になった時の処理
                    levelrole1 = discord.utils.get(message.server.roles, name="上級市民")
                    await target.add_roles(levelrole1)

        if message.author.bot:
            return

        conn=r.connect()
        p=conn.get("counter")
        p=str(p)
        p+=1
        ch=self.bot.get_channel(0)
        await ch.edit(name=f"message:{p}")
        q=conn.set("counter",p)
        print(q)

        if message.author.id != great_owner_id:
            return

        if message.content == 'ログ削除して':
            await message.channel.purge()
            msg = await message.channel.send("削除しました。")
            await asyncio.sleep(15)
            await msg.delete()

        if message.content == '再起動して':
            await self.bot.logout()

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(main(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
