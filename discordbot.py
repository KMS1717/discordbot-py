#main
from cmath import log
import discord
from dotenv import load_dotenv
import os
import api
load_dotenv()

#discord_token = 'MTIzOTA0OTY1NjEzOTI1MTczMw.G5SXUw.75nuzL5uVmp4nXaRdsAaTrx6uDWahrLBd_-gTuc'
#TOKEN = os.getenv(discord_token)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    await api.check_broad_period()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #!인사 명령어
    if message.content.startswith('!인사'):
        await message.channel.send('안녕하십니꺼행님치지직대표개쌉미남렘우니인사오지게박습니다!')

    #easterEgg
    if message.content.startswith('호치~'):
        await message.channel.send('아흣!')

    #!방송알림 시작 명령어        
    #if message.content.startswith('!방송알림 시작'):

try:
    client.run('MTIzOTA0OTY1NjEzOTI1MTczMw.Gk7NX6.xHTePiLkalhcVTezfvH77dwRC0igN97PzwkH_k')
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
