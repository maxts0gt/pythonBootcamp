import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter(indent=4)
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR SECRET"

# 1. TODO Choose which year to select
which_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# 2. TODO Crawling through top 100 songs on chosen date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{which_date}")
url = response.text

soup = BeautifulSoup(url, "html.parser")
songs = soup.select("span.chart-element__information__song")
artists = soup.select("span.chart-element__information__artist")
song_list = [song.getText() for song in songs]
artist_list = [artist.getText() for artist in artists]

# 3. TODO Authenticating with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path=".cache"))
current_user = sp.current_user()
spotify_id = current_user["id"]
# playlist_id = spotify_id


# 4. TODO Finding URIs for top 100 days from billboard list
tracks_uri = []
for i in range(len(songs)):
    try:
        track = (sp.search(f"track: {song_list[i]}, artist: {artist_list[i]}", type="track"))
        tracks_uri.append(track["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"There is no song called {song_list[i]} for Xmas on Spotify!")

# 5. TODO Creating a playlist
playlist_id = sp.user_playlist_create(user=spotify_id, name=f"{which_date} -> Billboard Best Songs!", public=False,
                                      description="This is Xmas for U")
new_playlist_id = (playlist_id["uri"])

sp.playlist_add_items(playlist_id=new_playlist_id, items=tracks_uri, position=None)

# 6. TODO Checking items and playlist id
playlist_items = sp.playlist_items(playlist_id=new_playlist_id)
print(new_playlist_id)
print(playlist_items)
