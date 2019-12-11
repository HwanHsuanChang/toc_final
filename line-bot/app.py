from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('d8St2HDsKdeJxIBHjLrMVqaW7UTHf6TymAXHjb7q0Bm6TfbGj4OsYXXrnDOcJmsrDY47Up5n3jeESnWNPwaFrG81Y3bDXno6SXBWbEGLnE1kQDl3aPNz825OHueNxdllQVi0XBgO3wJuoCxab4x5sAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('55ec82e62c03643b6a331fcd7b906925')

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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if ('a' in event.message.text) or ('b' in event.message.text) or ('c' in event.message.text) or ('d' in event.message.text) or ('e' in event.message.text) or ('f' in event.message.text) or ('g' in event.message.text) or ('h' in event.message.text) or ('i' in event.message.text) or ('j' in event.message.text) or ('k' in event.message.text) or ('l' in event.message.text) or ('m' in event.message.text) or ('n' in event.message.text) or ('o' in event.message.text) or ('p' in event.message.text) or ('q' in event.message.text) or ('r' in event.message.text) or ('s' in event.message.text) or ('t' in event.message.text) or ('u' in event.message.text) or ('v' in event.message.text) or ('w' in event.message.text) or ('x' in event.message.text) or ('y' in event.message.text) or ('z' in event.message.text) or ('A' in event.message.text) or ('B' in event.message.text) or ('C' in event.message.text) or ('D' in event.message.text) or ('E' in event.message.text) or ('F' in event.message.text) or ('G' in event.message.text) or ('H' in event.message.text) or ('I' in event.message.text) or ('J' in event.message.text) or ('K' in event.message.text) or ('L' in event.message.text) or ('M' in event.message.text) or ('N' in event.message.text) or ('O' in event.message.text) or ('P' in event.message.text) or ('Q' in event.message.text) or ('R' in event.message.text) or ('S' in event.message.text) or ('T' in event.message.text) or ('U' in event.message.text) or ('V' in event.message.text) or ('W' in event.message.text) or ('X' in event.message.text) or ('Y' in event.message.text) or ('Z' in event.message.text):
        message = TextSendMessage(text='bot: '+event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='機器人: '+event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
