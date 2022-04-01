import discord
import os
from discord.ext import commands
client=commands.Bot(command_prefix='?')



@client.event
async def on_ready():
    print ("bot is on line")
    channel=client.get_channel(int(906074499441655822))
    await channel.send('bot is online')


for filename in os.listdir('.vscode/uuu'):
    if filename.endswith('.py'):
        client.load_extension(f'uuu.{filename[:-3]}')

@client.command()
async def load(ctx,exten):
    client.load_extension(f'uuu.{exten}')
    await ctx.channel.send(f'\"{exten}\" has loaded')
@client.command()
async def unload(ctx,exten):
    client.unload_extension(f'uuu.{exten}')
    await ctx.channel.send(f'\"{exten}\" has unloaded')
@client.command()
async def reload(ctx,exten):
    client.reload_extension(f'uuu.{exten}')
    await ctx.channel.send(f'\'{exten}\' has reloaded')

 
client.run("OTA2MDY3NjA2MzEyNzE4Mzk2.YYTPNw.bx-iw3pu1aEDxxJyhbVYsagY-BU")
   