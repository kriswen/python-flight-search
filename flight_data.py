class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, from_city, from_code, to_code, to_city, from_date, to_date, price):
        self.from_city = from_city
        self.from_code = from_code
        self.to_city = to_city
        self.to_code = to_code
        self.from_date = from_date
        self.to_date = to_date
        self.price = price
