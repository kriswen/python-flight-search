# Flight Search Project

This project utilizes the Flight Search API to find the cheapest flights from a specified departure city to various destinations. It also provides notifications when the flight prices drop below the lowest prices listed in a Google Sheet.

## Description

This project consists of Python scripts that interact with the Flight Search API, Google Sheets API, and a notification service to provide flight information and notifications.

## Requirements

To run this project, you need:

- Python 3 installed on your system.
- A Kiwi API key for accessing the Flight Search API.
- A Google Sheets API key for accessing the Google Sheet with flight data.
- Telegram API credentials for sending message notifications.

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt

3. Set up your environment variables by creating a .env file in the root directory of the project and adding the necessary API keys and credentials:

   ```bash
    KIWI_API_KEY=your_kiwi_key
    SHEETY_TOKEN=your_sheety_token
    SHEETY_ENDPOINT=your_sheety_endpoint
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    TELEGRAM_CHAT_ID=your_chat_id

## Usage
1. Modify the main.py script with your desired settings, such as the departure city code, nights in destination, and any other parameters.
Run the main.py script:
2. Run the main.py script
3. The script will fetch flight data, update the Google Sheet with IATA codes, and send notifications for any price drops.
