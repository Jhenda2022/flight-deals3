import os
import requests

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class FlightData:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        '''Fetch data from google sheet.'''
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for row in self.destination_data:
            body = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_ENDPOINT}/{row['id']}",
                json=body
            )
