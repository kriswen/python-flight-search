import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData
import time

load_dotenv()
KIWI_API_KEY = os.environ.get("KIWI_API_KEY", "sheety endpoint url not exist")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # # https://tequila.kiwi.com/portal/docs/tequila_api/locations_api"
    def get_dest_code(self, city):
        # response from the FlightSearch class to update the sheet_data dictionary.
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "term": city,
            "location_types": "city",  # use city to get the city code ( cover multiple airports)
            "locale": "en - US",
            "limit": 1,
            "active_only": True,
        }
        response = requests.get(location_endpoint, headers=headers, params=query)
        response.raise_for_status()
        print(response.status_code)
        result = response.json()["locations"]
        city_code = result[0]["code"]
        return city_code

    def check_flights(self, from_city_code, to_city_code, from_date, to_date, nights_from,
                      nights_to):
        search_endpoint = f"{TEQUILA_ENDPOINT}/search"
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": nights_from,
            "nights_in_dst_to": nights_to,
            "one_for_city": 1,
            "max_stopovers": 0,
            "currency": "USD",
        }

        # print the city and price for all the cities in terminal
        try:
            # https://tequila.kiwi.com/portal/docs/user_guides/important_search_api_response_fields
            response = requests.get(search_endpoint, headers=headers, params=query)
            data = response.json()["data"][0]
            # print(data)
        except IndexError:
            print(f"No itinerary found for {to_city_code}.")
            return None

        flight_data = FlightData(
            from_city=data["route"][0]["cityFrom"],
            from_code=data["route"][0]["flyFrom"],
            to_city=data["route"][0]["cityTo"],
            to_code=data["route"][0]["flyTo"],
            # convert epoch time to human readable https://www.geeksforgeeks.org/convert-epoch-time-to-date-time-in-python/#google_vignette
            from_date=time.strftime("%Y-%m-%d", time.gmtime(data["route"][0]["dTime"])),
            to_date=time.strftime("%Y-%m-%d", time.gmtime(data["route"][1]["dTime"])),
            price=data["price"],
        )
        print(f"{flight_data.to_city}: ${flight_data.price}")
        # print(flight_data)
        return flight_data

