import os
import r
from discord.ext import commands
import discord
import random

class scythe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.namebea = 0
        self.givepoint = 0

    @commands.command(name="コンパス")
    async def compass_character(self, ctx, op=None):
        if op == None:
            cc=random.choice(("アタッカー","ガンナー","タンク","スプリンター"))
        else:
            cc=op
        conn=r.connect()
        pp=conn.smembers(cc)
        pp=[cv for cv in pp]
        gg=random.choice(pp)
        embed = discord.Embed(title=f"{ctx.author}さんの使うキャラは",description=None)
        embed.add_field(name=f"**タイプ**",value=f"`{cc}`")
        embed.add_field(name=f"**キャラ**",value=f"`{gg}`")
        await ctx.send(embed=embed)

    @commands.command(name="登録")
    async def sighin(self, ctx):
        """ポイント制度登録"""
        self.namebea = 0
        conn = r.connect()
        k = conn.keys()
        cai = str(ctx.author.id)
        for i in k:
            if i == cai:
                self.namebea += 1
        if self.namebea == 0:
            nb = conn.set(cai,"150")
            nb2 = conn.sadd("scythes",cai)
            if nb == True:
                await ctx.send("登録しました。\n登録特典で100Point付与しました。")   
            else:
                await ctx.send("登録に失敗しました。\nやり直して下さい。")
        else:
            await ctx.send("既に登録済みです。")

    @commands.command(name="ポイント確認")
    async def get_point(self, ctx, user_id:int= None):
        """ポイントの確認"""
        conn=r.connect()
        ci = str(ctx.author.id)
        gu = self.bot.get_user(user_id)
        ui = str(user_id)
        if user_id == None:
            embed = discord.Embed(title=f"**{ctx.author.name}さんの情報**", description=None)
            up = conn.get(ci)
            embed.add_field(name="現在ポイント", value=f"`{up}p`")
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title=f"**{gu.name}さんの情報**", description=None)
            up = conn.get(ui)
            embed.add_field(name="現在ポイント", value=f"`{up}p`")
            await ctx.send(embed=embed)
            return

    @commands.command(name="P制御")
    async def give_point(self, ctx, user_id:int=None, point:int=None):
        """ポイント付与・剥奪"""
        if user_id == None:
            return await ctx.send("ユーザーIDを設定して下さい。")
        if point == None:
            return await ctx.send("付与ポイントを設定して下さい。")
        self.givepoint = 0
        c = str(ctx.author.id)
        conn = r.connect()
        sm = conn.smembers('adomin')
        for ad in sm:
            if ad == c:
                self.givepoint += 1
        if self.givepoint == 0:
            return await ctx.send("貴方は操作できません。")
        un = self.bot.get_user(user_id)
        ui = str(user_id)
        up = conn.get(ui)
        up = int(up) + point
        us = conn.set(ui,up)
        if us == True:
            return await ctx.send(f"{un.name}さんに`{point}`P付与しました。")
        else:
            return await ctx.send("付与に失敗しました。\n最初からやり直して下さい。")

    @commands.command(name="ID取得")
    async def getid(self, ctx, user_mention:discord.Member=None):
        """ID確認用"""
        if user_mention == None:
            await ctx.send(f"{ctx.author.name}さんのidは")
            return await ctx.send(ctx.author.id)
        await ctx.send(f"{user_mention.name}さんのidは")
        await ctx.send(user_mention.id)

    @commands.command(name="ポイント管理者")
    async def point_admin(self, ctx):
        """ポイント管理者一覧"""
        P=1
        conn = r.connect()
        sm = conn.smembers('adomin')
        embed = discord.Embed(title=f"**ポイント管理者一覧**", description=None, color=0x9b59b6)
        for ad in sm:
            adm = self.bot.get_user(int(ad))
            embed.add_field(name=f"{P}人目", value=f"`{adm}`")
            P+=1
        await ctx.send(embed=embed)

    @commands.command(name="P集会付与")
    async def all_give_point(self, ctx):
        """集会参加ポイント"""
        self.givepoint = 0
        c = str(ctx.author.id)
        conn = r.connect()
        sm = conn.smembers('adomin')
        for ad in sm:
            if ad == c:
                self.givepoint += 1
        if self.givepoint == 0:
            return await ctx.send("貴方は操作できません。")
        mem=conn.smembers("scythes")
        for p in mem:
            q=ctx.guild.get_member(int(p))
            for ro in q.roles:
                if ro.name == "集会参加":
                    cg=conn.get(p)
                    bp=int(cg)+150
                    det=conn.set(p,bp)
        for am in ctx.guild.members:
            for adf in am.roles:
                prole = ctx.guild.get_role(709678662961594371)
                if adf.name == "集会参加":
                    await am.remove_roles(prole)
        
        await ctx.send("付与完了しました。")

    @commands.command(name="登録者")
    async def point_geter(self, ctx):
        """ポイント登録者一覧"""
        P=1
        conn = r.connect()
        sm = conn.smembers('scythes')
        embed = discord.Embed(title=f"**登録者**", description=None)
        for ad in sm:
            adm = self.bot.get_user(int(ad))
            embed.add_field(name=f"{P}人目", value=f"`{adm}`")
            P+=1
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(scythe(bot))
