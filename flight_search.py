import os
import requests
from flight_details import FlightDetails

TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_API = os.environ["TEQUILA_API"]

class FlightSearch:

    def get_destination_codes(self, city_name):
        '''Fetch codes of city from tequila.'''
        url = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {'apikey': TEQUILA_API}
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=url, headers=headers, params=params)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city, destination_city, date_from, date_to):
        '''Checks flights starting tomorrow up to six months. Returns details
        and populates flight_details.py'''
        url = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {'apikey': TEQUILA_API}
        query = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 0,
            "max_stopovers": 0,
            "curr": "USD",
        }
        response = requests.get(url=url, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
            data = response.json()["data"][0]
            fdet = FlightDetails(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                date_from=data["route"][0]["local_departure"].split("T")[0],
                date_to=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"],
                link=data['deep_link']
            )
            return fdet
        else:
            fdet = FlightDetails(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                date_from=data["route"][0]["local_departure"].split("T")[0],
                date_to=data["route"][1]["local_departure"].split("T")[0],
                link=data['deep_link']
            )
            return fdet
