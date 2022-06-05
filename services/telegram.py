import json
import os
import requests
import helpers


class Telegram:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.config = helpers.get_config()
        self.telegram_token = self.config["telegram_token"]
        self.URI = "https://api.telegram.org/bot{}/sendMessage".format(self.telegram_token)

    def send_msg(self, msg, keyboard):

        _data = {
            'chat_id': self.chat_id,
            'text': msg,
            'parse_mode': 'markdown',
        }

        if keyboard:
            _data['inline_keyboard'] = keyboard

        print(json.dumps(_data, indent=3))
        result = requests.post(self.URI, json=_data)
        print(result.status_code)
        print(result.content)

        if result.status_code != 200:
            return False

        return True
