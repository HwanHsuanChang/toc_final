import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("d8St2HDsKdeJxIBHjLrMVqaW7UTHf6TymAXHjb7q0Bm6TfbGj4OsYXXrnDOcJmsrDY47Up5n3jeESnWNPwaFrG81Y3bDXno6SXBWbEGLnE1kQDl3aPNz825OHueNxdllQVi0XBgO3wJuoCxab4x5sAdB04t89/1O/w1cDnyilFU=", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
