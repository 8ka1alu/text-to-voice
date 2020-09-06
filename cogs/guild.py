import discord
from discord.ext import commands

class sarver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        ch=guild.system_channel
        em = discord.Embed(title="**導入ありがとうございます**",description="このbotは管理者しか使うことができません\nPrefixは`e!`です", color=discord.Color.blue())
        if ch != None:
            await ch.send(embed=em)

    @commands.command()
    async def invite(self, ctx):
        invite="https://discord.com/api/oauth2/authorize?client_id=751714059652562966&permissions=8&scope=bot"
        sinvite="https://discord.gg/Jejvvpn"
        em = discord.Embed(title="**こちらから導入できます**",description=f"[このBOTの招待はこちら](<{invite}>)｜[サポート鯖はこちら](<{sinvite}>)", color=discord.Color.blue())
        await ch.send(embed=em)

def setup(bot):
    bot.add_cog(sarver(bot))
