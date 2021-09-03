import requests

# 1. TODO News Reader
numbering = 1
def news_reader():
    for article in articles:
        global numbering
        print("Tesla.Inc Related MOST READ 3 Articles:")
        print(f"{numbering}." + article["description"])
        numbering += 1

# 2. TODO Get stock market data and calculate the change
API_KEY = "YOUR API KEY"
url = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": API_KEY,
}

response = requests.get(url, params=parameters)
data = response.json()
A = float(data["Time Series (60min)"]['2021-09-02 20:00:00']['4. close'])  # Next day
B = float(data["Time Series (60min)"]['2021-09-01 20:00:00']['4. close'])  # Previous day
change = round(((A - B) / B) * 100, 2)

# 3. TODO Get news from news site and get top 3 news

url_news = "https://newsapi.org/v2/everything"
parameters_news = {
    "from": "2021-09-01T20:00:00",
    "q": ["Tesla", "TESLA", "TSLA"],
    "to": "2021-09-03T20:00:00",
    "sources": "bloomberg",
    "sortBy": "popularity",
    "apiKey": "YOUR API KEY",
    "pageSize": 3
}
response = requests.get(url_news, params=parameters_news)
articles = response.json()["articles"]

# 4. TODO Deliver market change and news

if A > B:
    print(f"TSLA: 🔻{change}%")
    news_reader()
else:
    print(f"TSLA: 🔺{change}%")
    news_reader()
