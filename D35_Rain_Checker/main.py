import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 43.263012,
    "lon": -2.934985,
    "appid": os.environ.get("OWN_API_KEY"),
    "exclude": "current,minutely,daily",
}

account_sid = "Your Account SID"
auth_token = os.environ.get("AUTH_TOKEN")


def checking_for_rain():
    for i in weather_between_0_to_12:
        if i["weather"][0]["id"] < 700:
            return True


response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
hourly_weather_data = response.json()["hourly"]
weather_between_0_to_12 = hourly_weather_data[0:12]

will_it_rain = checking_for_rain()
if will_it_rain:
    # 1. TODO Twilio Client
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️.",
            from_='Your Twilio Phone Number',
            to='+Your Phone Number'
        )

