import discord
from discord.ext import commands
import json
import random

with open('files.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

client=commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print ("bot is on line")
    channel=client.get_channel(int(906074499441655822))
    await channel.send('bot is online')
@client.command()
async def i(ctx):
    await ctx.send("gggg")
@client.command()
async def hi(ctx):
    await ctx.send("hi")

@client.command()
async def picture(ctx):
    ran_pic=random.choice(jdata['ran_pic'])
    await ctx.send(ran_pic)


client.run("OTA2MDY3NjA2MzEyNzE4Mzk2.YYTPNw.dbfJw_cBb7Wggllu8EQddjxQiy8")


