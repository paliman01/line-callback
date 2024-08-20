from flask import Flask, request, abort
from flask_restful import Resource
import json
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


class LineMessageApiWebhookController(Resource):
    def post(self):
        line_bot_api = LineBotApi(os.getenv('5v7FYwYR94oMw/4KAGOt3GpdNiMF4T/HuC2GJpFPV06DibGcTjwaMSd0tM3TuTGUoHu+IcWbOqz4LqdjLaHTqKOJg5I7dfmfP6AtchYj5IPbk1mxsJ2f8ZS+mlKviD7y9sqEEM+mFnS71HG1SMGrLQdB04t89/1O/w1cDnyilFU='))
        handler = WebhookHandler(os.getenv('e8c2e45c74674cef947c02cc35b9d985'))

        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']

        body = request.get_data(as_text=True)
        event = json.loads(body)
        print(event)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print(
                "Invalid signature. Please check your channel access token/channel secret.")
            abort(400)

        token = event['events'][0]['replyToken']
        if token == "00000000000000000000000000000000":
            pass
        else:
            line_bot_api.reply_message(token, TextSendMessage(
                text=event['events'][0]['message']['text']))
        return 'OK'
