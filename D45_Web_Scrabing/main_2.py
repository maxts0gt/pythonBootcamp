from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")
articles = (soup.findAll(name="a", class_='storylink'))

texts = []
links = []

for article_tag in articles:
    article_text = article_tag.getText()
    texts.append(article_text)
    article_link = article_tag.get("href")
    links.append(article_link)

upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

highest_votes = (upvotes.index([max(upvotes)][0]))

print(texts[highest_votes])
print(links[highest_votes])
print(upvotes[highest_votes])