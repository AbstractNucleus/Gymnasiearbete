import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

with open("/home/abstract/Gymnasiearbete/spotify/secrets", "r") as f:client_secret = f.read(); client_id = "166bf0427c28473385cfe53e316bec45"; sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

playlists = sp.user_playlists("weepur007")          # playlists["items"] returns a list of dictionaries that represents playlists
user = sp.user("weepur007")

songs = sp.playlist_items("5e7WkKA5MtmhHP0eK9wMFT")

song_ids = []
for i in songs["items"]:
    song_ids.append(i["track"].keys())

print(songs["items"][4]["track"].keys())