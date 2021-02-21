import discord
from discord.ext import commands
import json
import random,os,asyncio

intents = discord.Intents.default()
intents.members = True

#另外存取TOKEN
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '!', intents = intents)

#bot online
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#成員加入公會
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

#成員離開公會
@bot.event 
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

#ping 指令
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


bot.run(jdata['TOKEN'])