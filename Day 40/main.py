#This file will need to use the DataManager,FlightSearch,
#FlightData, NotificationManager classes to achieve the program requirements.


from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

flightData = FlightData()

#first update data with IATA code
#flightData.UpdateCityCode()

#print after got all citycode updated
#print(flightData.getCitiesData())

#add new city
flightData.uploadNewData()


#print last update
#print(flightData.getCitiesData)

#part where search for each flight and send msg if found
#flightSearch = FlightSearch()
#flightSearch.search()


#New part of Day 40 not all completed last part only not exist which is send to user via email
#Adding new user
""" Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
email = input("Enter your Email: ")
verifyEmail = input("Enter your email agian: ")
dataManager = DataManager()
if email == verifyEmail:
    dataManager.addUser(fname=Fname,lastname=Lname,email=email)
    print("You`r in the club") """
