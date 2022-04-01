import discord
import os
from discord.ext import commands
client=commands.Bot(command_prefix='?')



class cog (commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command()
    async def hi(ctx):
        await ctx.send("hi")   

def setup (client):
    client.add_cog(cog(client))