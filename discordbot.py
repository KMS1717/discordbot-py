#main
import discord
from dotenv import load_dotenv
import os
import requests
import time
import asyncio
from datetime import datetime
load_dotenv('token.env')

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID')) #디스코드 채널명

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

#방송아이디
broad_id = '319304cac96c224bd574b4ed930970e3'
channel_id = '1240332570474840115'

#api_url
chzzk_url = f'https://api.chzzk.naver.com/service/v2/channels/{broad_id}/live-detail'

#api 통신
def check_naver_status():
    response = requests.get(chzzk_url, headers={"User-Agent": "Mozilla/5.0"})
    
    # 전송 성공이면
    if response.status_code == 200:
        return response.json().get('content', {})
    else:
        print(f'Error Status code: {response.status_code}\nResponse: {response.text}')
        return None
    
#Naver Chzzk 방송 상태 확인 function
async def check_broad_period():
    # 봇이 준비될 때까지 대기
    await client.wait_until_ready() 
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        content_data = check_naver_status()

        if content_data:
            #reponse json 출력
            print(datetime.today().strftime("%Y/%m/%d %H:%M:%S")+" "+content_data.get('liveTitle'))

            #만약 현재 방송중이라면
            if content_data.get('status') == 'OPEN':

                title = content_data.get('liveTitle')
                channelName = content_data.get('channel').get('channelName')

                text_message = f'[치지직 라이브] {channelName}님의 방송이 시작되었습니다 !\n▶ 방송 제목: {title}\nhttps://chzzk.naver.com/live/{channel_id}'
                #channel.send(text_message)

                while check_naver_status().get('status') == 'OPEN':
                    print("현재 방송중입니다.")
                    time.sleep(30)
            
            else:
                print("현재 방송중이 아닙니다.")
        else:
            print("방송 정보를 가져오지 못했습니다.")
        
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_broad_period())

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
    client.run(DISCORD_TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
