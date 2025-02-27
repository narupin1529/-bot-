import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import random as rd
import requests

num = rd.randint(1,5)
n = str(num) #キーを文字列に変換してあげる

name_file = open("name.json","r",encoding="UTF-8")
file1= open("info.json","r") #lineのトークン
file2 = open("messages.json","r",encoding="utf-8")#text

name = json.load(name_file)
mes = json.load(file2)

main_kanmusu = name[n]#名前
main_contents = mes[main_kanmusu]
#print(main_contents[0])

text = main_contents[0] #テキスト
image_url = main_contents[1] #画像

info = json.load(file1)

ACCESS_TOKEN = info["TOKEN"]
line_bot_api = LineBotApi(ACCESS_TOKEN)

def main():
    USER_ID = info["ID"]
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    data = {
        'to': USER_ID,
        'messages': [
            {
                'type': 'image',
                'originalContentUrl': image_url,
                'previewImageUrl': image_url
            }
        ]
    }

    response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)

    messages = TextSendMessage(text=text)
    line_bot_api.push_message(USER_ID,messages=messages)


if __name__ == "__main__":
    main()
