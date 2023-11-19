""" A8_2vE!es-MkVuW :password for api of weather """
import json
import requests
import os
from twilio.rest import Client
""" api = "https://api.openweathermap.org/data/2.5/weather"
api_key = "288ee95f6588ee36b64c295bc2e71d90"
weather_params = {
    'lat':51.507351,
    'lon':-0.127758,
    'appid':api_key,
    'exclude':"current,minutely,daily",
} """

#req = requests.get(api,weather_params)

with open('data.json','r') as f:
    content = json.load(f)
    weather_info = content['weather']
    if weather_info[0]['id'] > 700:
        account_sid = 'AC7c9e1deecc929e9822732c2a8886e5f9'
        auth_token = '6f8fef7c39eec5b2d9b41a13a719c2cc'
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="it is hot today bring umberlla",
                     from_='+18702767596',
                     to='+201068430709'
                 )
    else:
        print('you good')
    #print(weather_info)



# Download the helper library from https://www.twilio.com/docs/python/install
""" 



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC7c9e1deecc929e9822732c2a8886e5f9']
auth_token = os.environ['6f8fef7c39eec5b2d9b41a13a719c2cc']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18702767596',
                     to='+201068430709'
                 ) """


