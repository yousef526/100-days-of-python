import requests
from datetime import datetime
import time
import smtplib as smtp

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_over():
    space_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    space_response.raise_for_status()
    space_data = space_response.json()

    iss_latitude = float(space_data["iss_position"]["latitude"])
    iss_longitude = float(space_data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    condition_1 = MY_LAT - iss_latitude <= 5 or  MY_LAT - iss_latitude >= -5
    condition_2 = MY_LONG - iss_longitude <= 5 or  MY_LONG - iss_longitude >= -5
    if condition_1 and condition_2:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    my_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    my_response.raise_for_status()
    my_data = my_response.json()
    sunrise = int(my_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(my_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset and time_now < sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




while True:
    if is_iss_over() and is_night():
        email = "20191700920@cis.asu.edu.eg"
        password = 'Wtdbe6A92pU7Rm9'
        with smtp.SMTP("smtp-outlock.com",port=587) as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="yousefalaa8190@gmail.com",
                msg="subject:ISS\n\n Look up"
            )
    time.sleep(60)


