from flight_data import FlightData
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notif import NotificationManager

nf = NotificationManager()
fs = FlightSearch()
fd = FlightData()
sheet_data = fd.get_destination_data()

ORIGIN_CITY = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = fs.get_destination_codes(row["city"])
        fd.destination_data = sheet_data
        fd.update_destination_codes()

tomorrow = datetime.now() + timedelta(1)
six_months = datetime.now() + timedelta(6*30)

for destination in sheet_data:
    flight = fs.check_flights(
        origin_city=ORIGIN_CITY,
        destination_city=destination["iataCode"],
        date_from=tomorrow,
        date_to=six_months
    )
    if flight.price < destination["lowestPrice"]:
        nf.telegram_bot_sendtext(
            bot_message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                        f" to {flight.destination_city}-{flight.desination_airport} from {flight.date_from} to {flight.date_to}"
        )