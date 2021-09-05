import requests
import os
from datetime import datetime, timedelta

# 1. TODO ######################NUTRITIONIX######################

GENDER = "male"
WEIGHT_KG = os.getenv("WEIGHT")
HEIGHT_CM = os.getenv("HEIGHT")
AGE = os.getenv("AGE")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("APP_KEY")
print(WEIGHT_KG, HEIGHT_CM, AGE, API_KEY, APP_ID)
AUTHENTICATION_SHEET = {
    "Authorization": os.getenv("Authorization")
}
print(AUTHENTICATION_SHEET)
exercise_endpoint = os.getenv("EXEC_END")
print(exercise_endpoint)
sheet_endpoint = os.getenv("SHEET_END")
print(sheet_endpoint)

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# 2. TODO ######################Sheety######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = (datetime.now() + timedelta(hours=9)).strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=AUTHENTICATION_SHEET)

    print(sheet_response.text)
