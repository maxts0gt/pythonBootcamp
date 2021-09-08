import requests
from bs4 import BeautifulSoup
from urllib3.util import url

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

#This will not work since the website is re-written in react. I will learn react and get back to it later in future!
#Till then.
# all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

movie_titles = [movie.getText() for movie in all_movies]

movies = (movie_titles[::-1])

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")