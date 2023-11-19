# one of important api(Appliaction programmble interface) aspects is API Endpoint 
import requests


"""
We have respones codes
1xx means hold on its loading
2xx means working
4xx means that the is error from client side
5xx means that the server has a problem"""

""" file = requests.get(url="http://api.open-notify.org/iss-now.json")
print(file.json())
file.raise_for_status() 
 """
param = {
    'lat':30.298482,
    'lng':31.776651,
    'formatted':0,
}
file = requests.get("https://api.sunrise-sunset.org/json",params=param)
file.raise_for_status()
data = file.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"Sunrise: {sunrise} \n Sunset: {sunset}")