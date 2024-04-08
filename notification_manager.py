import requests
import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_msg(self, message):
        bot_token = str(telegram_bot_token)
        bot_chat_id = str(telegram_chat_id)
        send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id +
                     '&parse_mode=Markdown&text=' + message)
        response = requests.get(send_text)
        return response.json()
