from discord.ext import commands, tasks # Bot Commands Frameworkをインポート
import traceback # エラー表示のためにインポート
import os
import discord

TOKEN = os.environ['DISCORD_BOT_TOKEN']
prefix = 'e!'

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.eval'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MyBot(commands.Bot):
    # MyBotのコンストラクタ。
    def __init__(self, command_prefix, help_command):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix,help_command)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print(self.user.name)  # ボットの名前
        print(self.user.id)  # ボットのID
        print(discord.__version__)  # discord.pyのバージョン
        print('----------------')
        await self.change_presence(status=discord.Status.idle,activity=discord.Game(name=f'EVAL|Ping:{self.ws.latency * 1000:.0f}ms')) 
 
class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")

#MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = MyBot(command_prefix='e!',help_command=JapaneseHelpCommand())
    bot.run(TOKEN)
