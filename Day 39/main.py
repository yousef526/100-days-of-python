#This file will need to use the DataManager,FlightSearch,
#FlightData, NotificationManager classes to achieve the program requirements.


from flight_data import FlightData
from flight_search import FlightSearch

#flightData = FlightData()

#first update data with IATA code
#flightData.UpdateCityCode()

#print after got all citycode updated
#print(flightData.getCitiesData())

#add new city
#flightData.uploadNewData()


#print last update
#print(flightData.getCitiesData)

#part where search for each flight and send msg if found
flightSearch = FlightSearch()
flightSearch.search()