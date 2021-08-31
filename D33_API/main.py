import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.566536  # Your latitude
MY_LONG = 126.977966  # Your longitude


def is_iss_overhead():
    response_of_location = requests.get("https://api.open-notify.org/json")
    response_of_location.raise_for_status()
    response_data = response_of_location.json()

    iss_latitude = float(response_data["iss_position"]["latitude"])
    iss_longitude = float(response_data["iss_position"]["longitude"])

    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (
            MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response_from_sunrise = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_from_sunrise.raise_for_status()
    response_data = response_from_sunrise.json()
    sunrise = int(response_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response_data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunrise + 9 > 24:
        sunrise = 24 - sunrise
        sunrise = 9 - sunrise
    else:
        sunrise = sunrise + 9
    if sunset + 9 > 24:
        sunset = 24 - sunset
        sunset = 9 - sunset
    else:
        sunset = sunset + 9
    time_now_hour = datetime.now().hour
    if (time_now_hour < sunset) and (time_now_hour > sunrise):
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="my_email", password="my_password!")
            connection.sendmail(
                from_addr="my_email",
                to_addrs="my_email",
                msg=f"Attention\n\nIt is on sky now"
            )
