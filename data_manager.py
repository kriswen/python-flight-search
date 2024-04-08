import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "sheety token not exist")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "sheety endpoint url not exist")
HEADERS = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
USE_LIVE_API = True


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_data = None

    def get_sheet_data(self):
        if USE_LIVE_API:
            response = requests.get(SHEETY_ENDPOINT, headers=HEADERS)
            response.raise_for_status()
            result = response.json()
        else:
            # sample result if trial api request is max out
            result = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                                 {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                                 {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                                 ]}
        self.sheet_data = result['prices']
        # print(pprint(self.sheet_data))
        return self.sheet_data

    def update_row_data(self, id):
        object_id = id
        # print(f"{SHEETY_ENDPOINT}/{object_id}")
        for city in self.sheet_data:
            if city.get("id") == object_id:
                data = {
                    "price": {
                        "iataCode": city["iataCode"]
                    }
                }
                put_response = requests.put(f"{SHEETY_ENDPOINT}/{object_id}", headers=HEADERS, json=data)
                print(put_response.text)
