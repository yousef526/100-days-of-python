from twilio.rest import Client
import requests

#This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self) -> None:
        self.account_sid = 'AC7c9e1deecc929e9822732c2a8886e5f9'
        self.auth_token = '6f8fef7c39eec5b2d9b41a13a719c2cc'

    def sendMsg(self,msg):
        client = Client(self.account_sid,self.auth_token)
        message = client.messages.create(
        body=msg,
        from_='+18702767596',
        to='+201068430709'
    )
    pass
    

    