from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime, timedelta
import data_manager
import flight_search
from notification_manager import NotificationManager
from user_manager import UserManager

load_dotenv()

fs = flight_search.FlightSearch()
dm = data_manager.DataManager()
sheet_data = dm.get_sheet_data()
notification_manager = NotificationManager()
user_manager = UserManager()

DEPARTURE_CITY_CODE = "SFO"
NIGHTS_IN_DEST_FROM = 7
NIGHTS_IN_DEST_TO = 28


def main():
    user_manager.get_user_data()
    print("Welcome to Kris's Flight Club.\nWe find the best flight deals and email you.")
    first_name = input("What is your first name?\n").title()
    last_name = input("What is your last name?\n").title()
    email = "temp1"
    email_confirm = "temp2"
    while email != email_confirm:
        email = input("What is your email?\n").lower()
        if email.lower() == "quite" or email.lower() == "exit":
            exit()
        email_confirm = input("Confirm your email again.\n").lower()
        if email_confirm.lower() == "quite" or email_confirm.lower() == "exit":
            exit()
    # add name to the Google sheet
    user_manager.add_user_data(first_name=first_name,
                               last_name=last_name,
                               email=email)

    # for row in sheet_data:
    #     # check is iataCode is empty, if so, pass to FlightSearch class to update
    #     if row["iataCode"] == "":
    #         # check for iata code
    #         row["iataCode"] = fs.get_dest_code(row["city"])
    #         # update new iataCode to gs for current row
    #         dm.update_row_data(row["id"])
    #         print(f"update iata for {row["city"]} is {row["iataCode"]}")
    #     # else:
    #     #     print(f"current iata for {row["city"]} is {row["iataCode"]}")
    # # pprint(dm.sheet_data)
    #
    # # Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later
    # date_tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    # date_six_month = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
    # # for all the cities in the Google Sheet.
    # for destination in sheet_data:
    #     # check price for each dest city using IATA code from google sheet
    #     destination_city_code = (destination["iataCode"])
    #     flight = fs.check_flights(
    #         from_city_code=DEPARTURE_CITY_CODE,
    #         to_city_code=destination_city_code,
    #         from_date=date_tomorrow,
    #         to_date=date_six_month,
    #         nights_from=NIGHTS_IN_DEST_FROM,
    #         nights_to=NIGHTS_IN_DEST_TO,
    #     )
    #     # If the price is lower than the lowest price listed in the Google Sheet then send a telegram message
    #     if flight.price < destination["lowestPrice"]:
    #         notification_manager.send_msg(
    #             f"Sent from your telegram bot - Low price alert! Only ${flight.price} to fly from"
    #             f" {flight.from_city}-{flight.from_code} to {flight.to_city}-{flight.to_code},"
    #             f" from {flight.from_date} to {flight.to_date}")


main()
