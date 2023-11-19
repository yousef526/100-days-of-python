import requests
from data_manager import DataManager

API = "https://api.tequila.kiwi.com/locations/query"
APIKEY = {
    'apikey':"pOXjNk2t-k5FEyDNl",
}
class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        self.dataManager = DataManager()
        self.flightdata = self.dataManager.getData()

    def getCityCode(self,city):
        data = {
            "term":city,   
        }
        res = requests.get(url=API,params=data,headers=APIKEY)
        code = res.json()['locations'][0]['code']
        print(code)
        return code

    def UpdateCityCode(self):
        for flight in self.flightdata:
            if flight['iataCode'] == '':
                iataCode = self.getCityCode(flight['city'])
                flight['iataCode'] = iataCode
                print(flight)
                self.dataManager.updateData(flight)

    def uploadNewData(self):
        city = input("Enter city Name: ")
        iatacode = self.getCityCode(city)
        price = int(input("Enter your lowest price: "))
        self.dataManager.postData(city=city,iatacode=iatacode,lowestPrice=price)

    def getCitiesData(self):
        return self.flightdata 


#x = FlightData()
#x.getCityCode('New York')
