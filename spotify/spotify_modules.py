import numpy as np
import pandas as pd
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

with open("/home/abstract/Gymnasiearbete/spotify/secrets", "r") as f:client_secret = f.read(); client_id = "166bf0427c28473385cfe53e316bec45"; sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


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


def save_user_data(user):
    print(get_songs("5e7WkKA5MtmhHP0eK9wMFT")[48])

























def get_user_playlists(user, playlists = []):
    for i in sp.user_playlists(user)["items"]:
        playlists.append({"name":i["name"],"id":i["id"]})
    return playlists

def get_artists(playlist, artists = []):
    for i in sp.playlist_items(playlist)["items"]:
        for j in i["track"]["artists"]:
            if j["name"] not in artists:
                artists.append([i["track"]["name"], {"name": j["name"], "id": j["id"], "genres": get_genres(j["name"])}])
    return artists

def get_user_artists(user, all_artists = []):
    for i in get_user_playlists(user):
        for j in get_artists(i["id"]):
            if j not in all_artists:
                all_artists.append(j)
    return all_artists

def get_all_genres(artists, all_genres = []):
    for i in artists:
        for j in get_genres(i):
            if j not in all_genres:
                all_genres.append(j)
    return all_genres

def save_genres(user):
    with open("spotify/genres.json", "r") as f:
        users = json.load(f)[0]
        genres = json.load(f)[1]
    if user in users:
        print("Genres have already been added from", user)
        exit()
    else:
        try:
            artists = get_user_artists(user)
            get_genres = get_all_genres(artists)
        except:
            print("Error when getting genres")
            exit()
        users.append(user)
        for i in get_genres:
            if i not in genres:
                genres.append(i)
        with open("spotify/genres.json", "w") as f:
            json.dump([users,genres], f)
        


'''with open("spotify/data.json", "r") as f: f = json.load(f)
for i in f:
    if user == i["name"]:
        print("User has already been added")
        exit()

playlists = get_user_playlists(user)

with open("spotify/data.json", "w") as file:
    f.append({
        "name": user,
        "playlists": playlists
    })'''
    
    