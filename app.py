from flask import Flask, request, abort

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

# 權杖
line_bot_api = LineBotApi('wWePWk+r0IuD5ayQPifBpwTW6AgRV3z+KrcoCL/2pwHtbSDyes8m7aOOKGdJBbFLL8gRXb+v8vnrvvzfMPuB/tuWobgXKAh1rHRztjMTbvRS/xgfI3piT4jemH9KrvgUpnjiucGjdp4xojxAh0iOHQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0ff48a175cf28bd57235a7089116e7e1')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我不知道你在說什麼，請再重新輸入！'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎？':
        r = '謝謝你！我吃過了～'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()