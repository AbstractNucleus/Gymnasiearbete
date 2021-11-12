import numpy as np
import pandas as pd
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2
import spotipy.util as util

with open("secrets", "r") as f:
    client_secret = f.read()
    client_id = "166bf0427c28473385cfe53e316bec45"
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def get_genres(artist):
    try:
        genres = []
        for i in sp.search(type="artist",q=artist)["artists"]["items"][0]["genres"]:
            genres.append(i)
    except:
        return genres
    return genres

def get_songs(playlist, songs = []):
    for i in sp.playlist_items(playlist)["items"]:
        artists = []
        for j in i["track"]["artists"]:
            genres = get_genres(j["name"])
            artists.append({"name": j["name"], "id": j["id"], "genres": genres})
        songs.append({"name": i["track"]["name"], "artists": artists})
    return songs

def get_playlists(user, playlists = []):
    for i in sp.user_playlists(user)["items"]:
        playlists.append({
            "name": i["name"],
            "id": i["id"],
            "songs": get_songs(i["id"])
        })
    return playlists

def get_50_recent_songs(user, recent_50_songs = []):
    scope = 'user-read-recently-played'
    redirect_uri = 'http://localhost:7777/callback'
    token = util.prompt_for_user_token(username=user,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    if not token:
        print("Couldn't get token")
        exit()
    sp = spotipy.Spotify(auth=token, auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    for i in sp.current_user_recently_played(limit=50)["items"]:
        artists = []
        for j in i["track"]["artists"]:
            genres = get_genres(j["name"])
            artists.append({"name": j["name"], "id": j["id"], "genres": genres})
        recent_50_songs.append({"name": i["track"]["name"], "artists": artists})
    return recent_50_songs

def get_50_top_artists(user, top_artists = []):
    scope = 'user-top-read'
    redirect_uri = 'http://localhost:7777/callback'
    token = util.prompt_for_user_token(username=user,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    if not token:
        print("Couldn't get token")
        exit()
    sp = spotipy.Spotify(auth=token, auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    for i in sp.current_user_top_artists(limit=50)["items"]:
        top_artists.append({
            "name": i["name"],
            "id": i["id"],
            "genres": get_genres(i["name"])
        })
    return top_artists





