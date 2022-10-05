import os
import urllib.parse
import requests

CUTT_API_KEY = os.environ["CUTT_API_KEY"]

class FlightDetails:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, date_from, date_to, link, stop_overs=0, via_city=""):
        '''Store details of flights.'''
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.date_from = date_from
        self.date_to = date_to
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.link = link

    def url_shortener(self, link):
        key = CUTT_API_KEY
        url = urllib.parse.quote(link)
        response = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url))
        short_url = response.json()["url"]["shortLink"]
        print(short_url)
        return short_url