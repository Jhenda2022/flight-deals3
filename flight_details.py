#Sample text below:
#Low price alert! Only $44 to fly fromLondon-STN toBerlin-BERfrom 2023-01-30 to 2023-02-01

class FlightDetails:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, date_from, date_to):
        '''Store details of flights.'''
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.desination_airport = destination_airport
        self.date_from = date_from
        self.date_to = date_to