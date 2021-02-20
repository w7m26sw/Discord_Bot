import discord
from discord.ext import commands
import json
import random,os,asyncio

intents = discord.Intents.default()
intents.members = True

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(812753320942108692)
    await channel.send(f'{member} join!')

@bot.event 
async def on_member_remove(member):
    channel = bot.get_channel(812751941473271848)
    await channel.send(f'{member} leave!')

bot.run(jdata['TOKEN'])