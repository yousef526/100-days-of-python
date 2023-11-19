import requests



API_SHEETY = "https://api.sheety.co/f9a1d0324ealsYousef/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.response = requests.get(url=API_SHEETY,)
    
    #return the json file that i will work on
    def getData(self):
        data = self.response.json()['prices']
        return data

    def postData(self,city,iatacode,lowestPrice):
        data = {
            "price": {
                "city": city,
                "iataCode": iatacode,
                'lowestPrice':lowestPrice,
            }
        }

        response = requests.post(url=API_SHEETY, json=data,)
        try:
            response.raise_for_status()
        except:
            print(response.status_code)
                

    # it will be used for only one time
    def updateData(self,data):
        print(data)
        newData = {
            "price": {
                "iataCode": data['iataCode'],
            }
        }
        endpoint = f"{API_SHEETY}/{data['id']}"
        response = requests.put(url=endpoint, json=newData,)

        response.raise_for_status()

    def addUser(self,fname,lastname,email):
        api = "https://api.sheety.co/f9a1db8515fdeousef/users"
        data = {
            "user": {
                "firstName": fname,
                "lastName": lastname,
                'email':email,
            }
        }

        response = requests.post(url=api, json=data,)
        try:
            response.raise_for_status()
        except:
            print(response.status_code)
     


"""
{'prices': [
    {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
    {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
    {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
    {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
    {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
    {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
    {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
    {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}   
"""
