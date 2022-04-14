import os

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
year = input("YEAR [YYYY] = ")
month = input("MONTH [MM] = ")
day = input("DAY [DD] = ")

DATE = f"{year}-{month}-{day}/"
URL = "https://www.billboard.com/charts/hot-100"
# "d737047e90464307975fada07827b1bb" "42211ac01cf441499b6fb3b184c88b31"
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
print(CLIENT_ID)
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

response = requests.get(f"{URL}/{DATE}")

soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all("h3", class_="a-no-trucate")
artists = soup.find_all("span", class_="a-no-trucate")
song_names = [song.getText().strip() for song in songs]
artist_names = [artist.getText().strip() for artist in artists]
song_uris = []
print(artist_names)

for song, artist in zip(song_names, artist_names):
    result = sp.search(q=f"track:{song} artist:{artist}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard V2", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
