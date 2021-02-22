import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):

    @commands.command()
    async def 好吃(self, ctx):
        pic = discord.File(jdata['Panda'])
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(React(bot))