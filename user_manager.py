import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "sheety token not exist")
SHEETY_USER_ENDPOINT = os.environ.get("SHEETY_USER_ENDPOINT", "sheety endpoint url not exist")
HEADERS = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
USE_LIVE_API = True


class UserManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.users_data = None

    def get_users_data(self):
        if USE_LIVE_API:
            response = requests.get(SHEETY_USER_ENDPOINT, headers=HEADERS)
            response.raise_for_status()
            users = response.json()
        else:
            # sample result if trial api request is max out
            users = {'users': [{'firstName': 'kris', 'lastName': 'wen', 'email': '123@gmail.com', 'id': 2},
                               {'firstName': 'peter', 'lastName': 'pan', 'email': '456@gmail.com', 'id': 3}]}
        self.users_data = users['users']
        return self.users_data

    def add_user_data(self, first_name, last_name, email):
        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        post_response = requests.post(f"{SHEETY_USER_ENDPOINT}", headers=HEADERS, json=user_data)
        post_response.raise_for_status()
        if post_response.status_code == 200:
            print("Success, your are now subscribed to the flight deals.")
        else:
            print(post_response.text)


