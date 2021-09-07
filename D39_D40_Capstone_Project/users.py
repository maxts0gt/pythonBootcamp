import requests
SHEETY_PUT = "YOUR SHEETY"
BASIC_TOKEN = "YOUR SECRET"


print("Welcome to Max's Flight Club.")
print("We find the best deals and email you.")

# 1. TODO Asking user info
keep_asking = True
first_name = input("What is your first name? ")
while keep_asking:
    if len(first_name) == 0:
        print("You should input your first name!")
        first_name = input("What is your first name? ")
    else:
        keep_asking = False
keep_asking = True
last_name = input("What is your last name? ")
while keep_asking:
    if len(last_name) == 0:
        print("You should input your last name!")
        last_name = input("What is your last name? ")
    else:
        keep_asking = False
keep_asking = True
email = input("What is your email? ")
email_validation = input("Type your email again. ")
while keep_asking:
    if email != email_validation:
        print("Emails don't match. Let's start again")
        email = input("What is your email? ")
        email_validation = input("Type your email again. ")
    else:
        keep_asking = False
print("Wonderful. You are in the \"Club\". \nFirst rule of club: Don't talk about club!.")


# 2. TODO Putting data into excel sheet with requests
params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}
headers = {
    "Authorization": BASIC_TOKEN
}

response = requests.post(url=SHEETY_PUT, json=params, headers=headers)
print(response.text)
