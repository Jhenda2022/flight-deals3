import os
import smtplib

import requests

BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
BOT_CHAT_ID = os.environ["TG_CHAT_ID"]
EMAIL_ADD = os.environ["EMAIL_ADD"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
REC_EMAIL = os.environ["REC_EMAIL"]

class NotificationManager:

    def send_emails(self, message):
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADD, password=EMAIL_PASS)
            connection.sendmail(from_addr=EMAIL_ADD,
                                to_addrs=REC_EMAIL,
                                msg=f"Subject:Low price alert!\n\n{message}"
                                )
