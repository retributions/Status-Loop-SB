import discord
from discord.ext import commands
import requests
import colorama
import json
import asyncio

with open('config.json', 'r') as f:
    config = json.load(f)

token = config.get('token')

watching_name = config.get('watching_name')

playing_name = config.get('playing_name')

listening_name = config.get('listening_name')

intents=discord.Intents.all()
intents.members = True

solar = commands.Bot(command_prefix='solar', self_bot=True, case_insensitive=False,intents=intents)
solar.remove_command('help')

@solar.event
async def on_connect():
  print('''
\033[0;32m╔═╗┌┬┐┌─┐┌┬┐┬ ┬┌─┐  ╦  ┌─┐┌─┐┌─┐\033[0m
\033[0;32m╚═╗ │ ├─┤ │ │ │└─┐  ║  │ ││ │├─┘\033[0m
\033[0;32m╚═╝ ┴ ┴ ┴ ┴ └─┘└─┘  ╩═╝└─┘└─┘┴  \033[0m
  ''')

@solar.event
async def on_ready():
  print("Status Loop Activated")
  await solarstatus()

async def solarstatus():
    while True:
        await solar.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name=watching_name))
        await asyncio.sleep(60)
        await solar.change_presence(status=discord.Status.idle,activity=discord.Game(name=playing_name))
        await asyncio.sleep(60)
        await solar.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.listening,name=listening_name))
        await asyncio.sleep(60)


solar.run(token, bot=False)
