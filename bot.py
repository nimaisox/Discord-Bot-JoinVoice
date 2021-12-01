import discord
from discord.ext import commands
from discord.utils import get
import os

token = 'TOKEN-BOT'

bot = commands.Bot(command_prefix='PREFIX')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(token)