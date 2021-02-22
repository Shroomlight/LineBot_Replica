from flask import Flask, request, abort, logging

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('gd8r9kQxyrGZrb4phBaA57fHMWY/P9jbMlX5O7REEYn9z3og6TvYtX5WyENXYOKBx0BL3LmumGNaTkOfSpNakhz+aqsd9d2vUCr7SbFH1saibQFwGOO0KHQu5JnAJNAqQYYZp+DVfVwj5Q22+OHY7AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ee758ba343a9fd7603ad160831a25a4f')


@app.route("/")
def home():
    return 'home OK'

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
    