# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import errno
import os
import sys
import subprocess
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

displayClockPropen = 0
stasts = 0
app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise


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
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    global displayClockPropen
    global stasts

    if text == 'quit':
        stasts = 0
    if stasts == 1:
        errStasts = 0
        time = text.split(":", 2)
        hour = int(time[0])
        minute = int(time[1])
        if (hour < 0 or hour > 23):
            errStasts = errStasts + 1
        if (minute < 0 or minute > 59):
            errStasts = errStasts + 2
        if errStasts == 1:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='時間は00〜23時でお願い\n"quit"で戻るよ'))
        elif errStasts == 2:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='分は00〜59分でお願い\n"quit"で戻るよ'))
        elif errStasts == 3:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='時間は0〜23時でお願い\n分は0〜59分でお願い\n"quit"で戻るよ'))
        else:
            stasts = 0
            cmd = "at %02d:%02d -f ../alerm.sh"%(hour, minute)
            subprocess.run(cmd, shell=True)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='%02d:%02dにセットしたよ'%(hour, minute)))
    elif text == 'ON!':
        if displayClockPropen == 0:
            displayClockPropen = subprocess.Popen(['python3', '../DisplayClock.py'])
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='点灯したよ'))
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='点灯してるよ'))
    elif text == 'OFF!':
        if displayClockPropen == 0:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='点灯してないよ'))
        else:
            subprocess.Popen(['kill ' '-s ' '2 ' '%d'%(displayClockPropen.pid)], shell=True)
            displayClockPropen = 0
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='消灯したよ'))
    elif text == 'Alarm!':
        subprocess.Popen('.././alerm.sh', shell=True)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='アラーム ON'))
    elif text == 'Alarm':
        stasts = 1
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='いつ起こして欲しいの?? (hh:mmで教えてね)'))
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    # create tmp dir for download content
    make_static_tmp_dir()

    app.run(debug=options.debug, port=options.port)
