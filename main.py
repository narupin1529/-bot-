import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import random as rd

num = rd.randint(1,3)

file1= open("info.json","r")
file2 = open("messages.json","r",encoding="utf-8")
info = json.load(file1)
mes = json.load(file2)

ACCESS_TOKEN = info["TOKEN"]
line_bot_api = LineBotApi(ACCESS_TOKEN)

def main():
    num = rd.randint(1,3)
    USER_ID = info["ID"]
    n = str(num) #キーを文字列に変換してあげる
    messages = TextSendMessage(text=mes[n])
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__ == "__main__":
    main()