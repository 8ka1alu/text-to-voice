import discord
from discord.ext import commands

class sarver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        chs=[c for c in guild.channels]
        ch=chs[0]
        em = discord.Embed(title="**導入ありがとうございます**",description="このbotは管理者しか使うことができません", color=discord.Color.blue())
        await ch.send(embed=em)

def setup(bot):
    bot.add_cog(sarver(bot))
