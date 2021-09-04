import requests
from datetime import datetime, timedelta

USERNAME = "YOUR NAME"
TOKEN = "YOUR TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "pages",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# #

today = datetime.now() - timedelta(days=1) #Minus 1 day
new_today = str(today.strftime("%Y%m%d"))

post_config = {
    "date": new_today,
    "quantity": input("How many books did you read today?"),
}

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.put(url=post_endpoint, json=post_config, headers=headers)

update_config = {
    "quantity": "8",
}

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{new_today}"
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{new_today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)