import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    #ping 指令
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    #log 指令
    @commands.command()
    async def log(self, ctx):
        async for entry in guild.audit_logs(limit=1):
            print('{0.user} did {0.action} to {0.target}'.format(entry))    

def setup(bot):
    bot.add_cog(Main(bot))