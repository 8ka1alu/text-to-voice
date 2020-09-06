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

    @commands.command(description="※招待")
    async def invite(self, ctx):
        em = discord.Embed(title="**こちらから導入できます**",description=None, color=discord.Color.blue())
        
def setup(bot):
    bot.add_cog(sarver(bot))
