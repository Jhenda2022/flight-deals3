import os

import requests

BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
BOT_CHAT_ID = os.environ["TG_CHAT_ID"]

class NotificationManager:

    def telegram_bot_sendtext(self, bot_message):
        '''Sends message using telegram bot.'''
        send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + \
                    '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()
