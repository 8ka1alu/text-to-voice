from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class info(commands.Cog):
    # infoクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['sinfo'])
    async def serverinfo(self, ctx, server_id: int=None):
        """鯖について"""
        if server_id == None:
            embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
            embed.add_field(name="サーバー名",value=f'`{ctx.guild.name}`')
            embed.add_field(name="現オーナー名",value=f'`{ctx.guild.owner}`')
            guild = ctx.guild
            embed.add_field(name="作成日",value=f'`{guild.created_at}`')
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
            embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
            embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
            embed.add_field(name="テキストチャンネル数",value=f'`{len(ctx.guild.text_channels)}`',inline=False)
            embed.add_field(name="ボイスチャンネル数",value=f'`{len(ctx.guild.voice_channels)}`',inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)
            return
        server = self.bot.get_guild(server_id)
        embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="サーバー名",value=f'`{server.name}`')
        embed.add_field(name="現オーナー名",value=f'`{server.owner}`')
        embed.add_field(name="作成日",value=f'`{server.created_at}`')
        guild = server
        member_count = sum(1 for member in guild.members if not member.bot) 
        bot_count = sum(1 for member in guild.members if member.bot) 
        all_count = (member_count) + (bot_count)
        embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
        embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
        embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
        embed.add_field(name="テキストチャンネル数",value=f'`{len(server.text_channels)}`',inline=False)
        embed.add_field(name="ボイスチャンネル数",value=f'`{len(server.voice_channels)}`',inline=False)
        embed.set_thumbnail(url=server.icon_url)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['b'])
    async def bot(self, ctx):
        """Botについて"""
        embed = discord.Embed(title=f"{self.bot.user}", description="このBotの情報です")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="SERVERの数", value=f'`{len(self.bot.guilds)}`',inline=False)
        embed.add_field(name="USERの数", value=f'`{len(set(self.bot.get_all_members()))}`',inline=False)
        embed.add_field(name="言語", value='`discord.py`\n`discord.js`',inline=False)
        embed.add_field(name="Ping値", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
        embed.add_field(name="各種リンク", value="[このBOTの公式開発鯖](<https://discord.gg/ENxnsJM>)", inline=False)
        await ctx.channel.send(embed=embed)
            
    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, user_id=None):
        """ユーザーについて"""
        if user_id == None:
            memberss = self.bot.get_user(ctx.author.id)
            embed = discord.Embed(title="プロフィール", description=None)
            embed.set_thumbnail(url=memberss.avatar_url)
            embed.add_field(name="Name", value=f'`{memberss.name}`',inline=False)
            embed.add_field(name="Tag", value=f"`{memberss.discriminator}`", inline=False)
            embed.add_field(name="ID", value=f'`{memberss.id}`',inline=False)
            embed.add_field(name="bot", value=f'`{memberss.bot}`',inline=False)
            embed.add_field(name="Create Account", value=f'`{memberss.created_at}`',inline=False)
            embed.add_field(name="Ping", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
            await ctx.channel.send(embed=embed)
            return
        user = await self.bot.fetch_user(int(user_id))
        embed = discord.Embed(title="**User Information**", description=None)
        embed.set_thumbnail(url=user.avatar_url_as(static_format="png"))
        embed.add_field(name="Name", value=f'`{user.name}`',inline=False)
        embed.add_field(name="Tag", value=f"`{user.discriminator}`", inline=False)
        embed.add_field(name="ID", value=f'`{user.id}`',inline=False)
        embed.add_field(name="bot", value=f'`{user.bot}`',inline=False)
        embed.add_field(name="Create Account", value=f'`{user.created_at}`',inline=False)
        embed.add_field(name="Ping", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
        await ctx.send(embed=embed)
        if user.bot == False:
            up = self.bot.fetch_profile(int(user))
            embed = discord.Embed(title="プロフィール", description=None)
            embed.set_thumbnail(url=user.avatar_url_as(static_format="png"))
            embed.add_field(name="ニトロの有無", value=f'`{up.premium}`',inline=False)
            embed.add_field(name="ニトロ日", value=f'`{up.premium_since}`',inline=False)
            embed.add_field(name="スタッフ", value=f'`{up.staff}`',inline=False)
            embed.add_field(name="パートナー", value=f"`{up.partner}`", inline=False)
            embed.add_field(name="デバッガー", value=f'`{up.bug_hunter}`',inline=False)
            await ctx.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(info(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。        
