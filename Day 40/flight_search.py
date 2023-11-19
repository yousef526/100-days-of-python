import requests
from data_manager import DataManager
from notification_manager import NotificationManager
import datetime as dt

API = "https://api.tequila.kiwi.com/v2/search"
APIKEY = {
    'apikey':"pOXjNk2t-k5wef8VsQApGV8rx5FEyDNl",
}
SRC = "LON"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.dataManager = DataManager()
        self.flightdata = self.dataManager.getData()
        self.notication_send = NotificationManager()

    
    def search(self):
        now = dt.datetime.now()
        after_6month = now + dt.timedelta(days=6*30)
        after_6month = after_6month.strftime("%d/%m/%Y")
        for flight in self.flightdata:
            try:
                params = {
                    "fly_from":SRC,
                    "fly_to":flight['iataCode'],
                    "date_from":now.strftime("%d/%m/%Y"),
                    "date_to":after_6month,
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 30,
                    "flight_type": "round",
                    "one_for_city": 1,
                    "max_stopovers": 0,
                    "curr": "GBP"
                }
                res = requests.get(url=API,headers=APIKEY,params=params)
                price = res.json()['data'][0]['price']
                data = res.json()['data'][0]["route"]
            except IndexError:
                continue
            else:
                flyTo = data[0]["flyTo"]
                flyFrom = data[0]["flyFrom"]
                cityTo = data[0]["cityTo"]
                cityFrom = data[0]["cityFrom"]
                local_departure = res.json()['data'][0]["local_departure"].split("T")[0]
                local_arrival = res.json()['data'][0]["local_arrival"].split("T")[0]

                if flight["lowestPrice"] > price:
                    print(flight['iataCode'])
                    msg=f"""
                    Low pricem alert! only ${price} to fly from {cityFrom}-{flyFrom} to 
                    {cityTo}-{flyTo}, from {local_departure} to {local_arrival}
                    """
                    self.notication_send.sendMsg(msg=msg)
                #print(data)
                #break
            

