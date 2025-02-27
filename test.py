import requests
import json


file1= open("info.json","r")
file1= open("info.json","r")
file2 = open("messages.json","r",encoding="utf-8")
info = json.load(file1)
mes = json.load(file2)

ACCESS_TOKEN = info["TOKEN"]

USER_ID = info["ID"]


image_url = 'https://drive.google.com/uc?id=1sZeiLkF0GamiY1Wle6q3D1eEwTXzQF2F'

# メッセージデータの作成
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

# リクエストの送信
response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)
