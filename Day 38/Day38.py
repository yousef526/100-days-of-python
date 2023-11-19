# nutriion website pass 123456ABDC789!@#$
# ID: 4a4fb195
# Key: c30ccdba428591b06db04bf6dccf978e

import requests
import datetime as dt

APPID = "4a4fb195"
KEY = "c30ccdba428591b06db04bf6dccf978e"
user = input("Enter your activity: ")

exercise_headers = {
    "x-app-id":APPID,
    "x-app-key":KEY,
    "Content-Type":"application/json",
}

exercise_params = {
    "query":user,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}

response1 = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         headers=exercise_headers,
                         json=exercise_params)

#print(response1.json())

apiSheety = "https://api.sheety.co/f9a1db8515fde64af74327d98f8b0324/workoutSheetYousef/workouts"


AuthorizationHeader = {
    'Authorization':"Bearer 123459ABDCsdsc!@#asd"
}
for element in response1.json()['exercises']:
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")

    exercise_type = element['user_input']
    duration = element['duration_min']
    calories = element['nf_calories']
    
    data_needed = {
        "workout":{
            'date':date,
            'time':time,
            'exercise':exercise_type,
            'duration':duration,
            'calories':calories,
        }
    }
    response2 = requests.post(url=apiSheety,json=data_needed,headers=AuthorizationHeader)
    print(response2.json())


