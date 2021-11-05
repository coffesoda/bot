import discord
from discord.ext import commands
client=commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print ("bot is on line")
    channel=client.get_channel(int(906074499441655822))
    await channel.send('bot is online')
@client.command()
async def i(ctx):
    await ctx.send("gggg")


client.run("OTA2MDY3NjA2MzEyNzE4Mzk2.YYTPNw.iGShD3dbum8cbXcPYMpkJ-1SXN4")


