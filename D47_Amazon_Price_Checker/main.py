import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 75.00

URL = "https://www.amazon.com/SanDisk-1TB-Extreme-Portable-SDSSDE61-1T00-G25/dp/B08GTYFC37/ref=sr_1_38?dchild=1&qid=1631216238&s=computers-intl-ship&sr=1-38"

test_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
params = {
    "Accept-Language": "en-US,en;q=0.9,mn-MN;q=0.8,mn;q=0.7,ko-KR;q=0.6,ko;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

response = requests.get(url=URL, headers=params)

soup = BeautifulSoup(response.text, parser=lxml, features="lxml")

price = soup.select(".priceBlockBuyingPriceString")
price = [p.getText().split("$")[1] for p in price][0]
price_as_float = float(price)

print(type(price))
title = "Go Buy it! from Future YOU!"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
