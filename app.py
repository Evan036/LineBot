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

line_bot_api = LineBotApi('XEhpzjXwQ93vagVrj7hOq6BLOvg5dyXnJw7OGtm4ZMUexqBAvLQP9hpoXfukpIkTYgSl+QyWv4H8otvWSF2i3ms3PRcTfoue50TeGXrhPeLnedlR/38oqgMOGl1KGCKnmOLClCl1/fo/K6DXQ28LNwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6988909999d35600360ee8580b9b28fc')


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
    reply_msg= '我不懂你說的, 我只知道Evan是救世主. 信主得永生!!'
    if msg == 'hi':
        reply_msg = '是的, 謝謝你成為Evan的粉絲!'
    elif msg == 'hello':
        reply_msg = '沒錯, Evan是天才!! 謝謝你!!'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()