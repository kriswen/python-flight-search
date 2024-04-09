class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, origin_city, origin_airport_code, dest_airport_code, dest_city, outbound_date, return_date, price, stop_over=0, via_city=""):
        self.from_city = origin_city
        self.from_code = origin_airport_code
        self.to_city = dest_city
        self.to_code = dest_airport_code
        self.from_date = outbound_date
        self.to_date = return_date
        self.price = price
        self.stop_over = stop_over
        self.via_city = via_city
