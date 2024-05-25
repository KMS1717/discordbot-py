from cmath import log
import discord
from dotenv import load_dotenv
import os
load_dotenv()

#discord_token = 'MTIzOTA0OTY1NjEzOTI1MTczMw.G5SXUw.75nuzL5uVmp4nXaRdsAaTrx6uDWahrLBd_-gTuc'
#TOKEN = os.getenv(discord_token)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!call':
        await message.channel.send("callback!")

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


try:
    client.run('MTIzOTA0OTY1NjEzOTI1MTczMw.Gk7NX6.xHTePiLkalhcVTezfvH77dwRC0igN97PzwkH_k')
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")

