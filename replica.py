from flask import Flask, request, abort, logging, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import json

import codecs

import urllib.request as urlrequest

import urllib.parse as parse

import os

app = Flask(__name__)

line_bot_api = LineBotApi('gd8r9kQxyrGZrb4phBaA57fHMWY/P9jbMlX5O7REEYn9z3og6TvYtX5WyENXYOKBx0BL3LmumGNaTkOfSpNakhz+aqsd9d2vUCr7SbFH1saibQFwGOO0KHQu5JnAJNAqQYYZp+DVfVwj5Q22+OHY7AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ee758ba343a9fd7603ad160831a25a4f')

# 訪問clock.html
@app.route("/")
def home():
    return render_template("clock.html")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent)
def handle_message(event):
    message_type = event.message.type
    user_id = event.source.user_id
    reply_token = event.reply_token
    message = event.message.text
    if "天氣" in message:
        #擷取並轉換城市名稱
        cityName=message[0:3]
        cityNameUrl=parse.quote(cityName) #轉換成URL型態
        cwbdata="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-850C0B7B-8172-4E44-AE39-5023FC83C899&locationName="+cityNameUrl
        
        #打開CWB的json資料
        with urlrequest.urlopen(cwbdata) as response :
            data=json.load(response)
        value=data["records"]["location"][0]['weatherElement'][0]['time'][0]['parameter']['parameterValue']
        startTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['startTime'])
        endTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['endTime'])
        #讀取預設主題
        weatherFlex=json.load(codecs.open("./weatherFlex/weather.json","r+","utf-8-sig"))
        
        #修改非變數資料
        #縣市名稱
        weatherFlex["contents"][0]["body"]["contents"][0]["text"]=cityName
        #天氣狀況
        weatherFlex["contents"][0]["body"]["contents"][1]["text"]=data["records"]["location"][0]['weatherElement'][0]['time'][0]['parameter']['parameterName']
        #溫度顯示
        weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][1]["text"]="溫度："+str((int(data["records"]["location"][0]['weatherElement'][4]['time'][0]['parameter']['parameterName'])+int(data["records"]["location"][0]['weatherElement'][2]['time'][0]['parameter']['parameterName']))/2)+"°C"
        #最高最低溫度
        weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][2]["text"]=data["records"]["location"][0]['weatherElement'][4]['time'][0]['parameter']['parameterName']+"°C"+" / "+data["records"]["location"][0]['weatherElement'][2]['time'][0]['parameter']['parameterName']+"°C"
        #降雨機率
        weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][1]["text"]="降雨機率："+data["records"]["location"][0]['weatherElement'][1]['time'][0]['parameter']['parameterName']+"%"
        #降雨提醒
        num = weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][1]["text"]
            #運用降雨提醒的字數差調配提醒
        if (int(num[5:len(num)-1])) < 20:
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]="機率極低"
        elif (int(num[5:len(num)-1])) < 40:
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]="機率低"
        elif (int(num[5:len(num)-1])) < 60:
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]="建議配傘"
        elif (int(num[5:len(num)-1])) < 80:
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]="需配傘"
        else:
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]="減少外出！"
        #舒適度
        weatherFlex["contents"][0]["body"]["contents"][3]["contents"][0]["text"]="舒適度："+data["records"]["location"][0]['weatherElement'][3]['time'][0]['parameter']['parameterName']
        #時間區段顯示
        startTime=data["records"]["location"][0]['weatherElement'][0]['time'][0]['startTime']
        endTime=data["records"]["location"][0]['weatherElement'][0]['time'][0]['endTime']
        weatherFlex["contents"][0]["body"]["contents"][4]["text"]=startTime[0:4]+" / "+startTime[5:7]+" / "+startTime[8:10]+" "+startTime[11:16]+"至"+endTime[11:16]
        #改變變數資料-判斷主題顏色（偏晴天）
        if int(value) <= 2:
            #天氣圖片
            weatherFlex["contents"][0]["hero"]["url"]="https://i.imgur.com/ox26zSo.png"
            #溫度計icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["url"]="https://i.imgur.com/WhbVYFp.png"
            #降雨量icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][0]["url"]="https://i.imgur.com/JS57GtP.png"
            #按鈕顏色
            weatherFlex["contents"][0]["footer"]["contents"][0]["color"]="#FF6B6E"
        #改變變數資料-判斷主題顏色（偏多雲）
        elif int(value) <= 5:
            #天氣圖片
            weatherFlex["contents"][0]["hero"]["url"]="https://i.imgur.com/9oXJkit.png"
            #溫度計icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["url"]="https://i.imgur.com/vvrAu5w.png"
            #降雨量icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][0]["url"]="https://i.imgur.com/iIfZljm.png"
            #按鈕顏色
            weatherFlex["contents"][0]["footer"]["contents"][0]["color"]="#7BCEF5"
        #改變變數資料-判斷主題顏色（偏陰天）
        elif int(value) > 5:
            #天氣圖片
            weatherFlex["contents"][0]["hero"]["url"]="https://i.imgur.com/tUyO4Bf.png"
            #溫度計icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["url"]="https://i.imgur.com/Z1aN0ak.png"
            #降雨量icon
            weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][0]["url"]="https://i.imgur.com/wirHtf5.png"
            #按鈕顏色
            weatherFlex["contents"][0]["footer"]["contents"][0]["color"]="#AAB5C0"
            
        #重寫入天氣設定
        newData = json.dumps(weatherFlex,ensure_ascii=False)
        os.remove("./weatherFlex/weatherFlex.json")
        newFile=open("./weatherFlex/weatherFlex.json",mode="w",encoding="utf-8")
        newFile.write(str(newData))
        newFile.close()

        FlexMessage_Weather = json.load(codecs.open('./weatherFlex/weatherFlex.json','r','utf-8-sig'))

        line_bot_api.reply_message(reply_token, FlexSendMessage('屏東市天氣',FlexMessage_Weather))
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))


if __name__ == "__main__":
    app.run()
    