#api.py
import requests
import time
import discord
from datetime import datetime

#url = 'https://api.chzzk.naver.com/service/v2/channels/b044e3a3b9259246bc92e863e7d3f3b8/live-detail'
#response = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})

#if response.status_code == 200:
#    data = response.json()
#    print(data)
#    #print(json.dump(data, indent=4)) #데이터 이쁘게보이게하기

#else:
#    print("Request failed with status code:", response.status_code)

#방송아이디
broad_id = '319304cac96c224bd574b4ed930970e3'
channel_id = '1240332570474840115'

#api_url
chzzk_url = f'https://api.chzzk.naver.com/service/v2/channels/{broad_id}/live-detail'

def check_naver_status():
    response = requests.get(chzzk_url,headers={"User-Agent":"Mozilla/5.0"})
    
    #전송성공이면
    if response.status_code == 200:
        return response.json().get('content', {})
    else:
        print(f'Error Status code: {response.status_code}\nResponse: {response.text}')
        return None

#Naver Chzzk 방송 상태 확인 function
def check_broad_period():

    while True:
        content_data = check_naver_status()

        #reponse json 출력
        print(datetime.today().strftime("%Y/%m/%d %H:%M:%S")+" "+content_data.get('liveTitle'))
        #print(content_data)

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
            time.sleep(10)
