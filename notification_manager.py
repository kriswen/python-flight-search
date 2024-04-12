import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")
email_sender = os.environ.get("MY_EMAIL")
email_password = os.environ.get("MY_EMAIL_PASSWORD")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_msg(self, message):
        bot_token = str(telegram_bot_token)
        bot_chat_id = str(telegram_chat_id)
        send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id +
                     '&parse_mode=Markdown&text=' + message)
        response = requests.get(send_text)
        return response.json()

    def send_email(self, subscriber_name, subscriber_email, message):
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
            connection.starttls()  # transfer layer security
            connection.login(user=email_sender, password=email_password)
            connection.sendmail(from_addr=email_sender,
                                to_addrs=subscriber_email,
                                msg=f"Subject: Flight Deal Alert!\n\nHi {subscriber_name}:\n{message}")
