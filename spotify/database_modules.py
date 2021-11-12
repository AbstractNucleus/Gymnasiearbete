import numpy as np
import pandas as pd
import json, spotipy, os, operator, collections

with open("secrets", "r") as f:
    client_secret = f.read()
    client_id = "166bf0427c28473385cfe53e316bec45"
    sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    redirect_uri = 'http://localhost:7777/callback'

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

def get_recent_songs(user, recent_50_songs = []):
    scope = 'user-read-recently-played'
    token = spotipy.util.prompt_for_user_token(username=user,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    if not token:
        print("Couldn't get token")
        exit()
    sp = spotipy.Spotify(auth=token, auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    for i in sp.current_user_recently_played(limit=50)["items"]:
        artists = []
        for j in i["track"]["artists"]:
            genres = get_genres(j["name"])
            artists.append({"name": j["name"], "id": j["id"], "genres": genres})
        recent_50_songs.append({"name": i["track"]["name"], "artists": artists})
    return recent_50_songs

def get_top_artists(user, top_artists = []):
    scope = 'user-top-read'
    token = spotipy.util.prompt_for_user_token(username=user,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    if not token:
        print("Couldn't get token")
        exit()
    sp = spotipy.Spotify(auth=token, auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    for i in sp.current_user_top_artists(limit=50)["items"]:
        top_artists.append({
            "name": i["name"],
            "id": i["id"],
            "genres": get_genres(i["name"])
        })
    return top_artists

def get_favourite_genres(user, favourite_genres = []):
    with open("data/database.json", "r") as f:
        f = json.load(f)
    for i in f:
        if i["name"] != user:
            print("User not found")
            exit()
        user_data = i
    genres = []
    for artist in user_data["top_artists"]:
        for genre in artist["genres"]:
            genres.append(genre)
    genres = dict(collections.Counter(genres))
    for i in range(10):
        highest = max(genres.items(), key=operator.itemgetter(1))[0]
        favourite_genres.append(highest)
        del genres[highest]
    return favourite_genres

def save_user_data(user):
    with open("data/database.json", "r") as f:
        f = json.load(f)
    for i in f:
        if i["name"] == user:
            print("User has already been added")
            exit()
    f.append({
        "name": user,
        "playlists": get_playlists(user),
        "recently_played": get_recent_songs(user),
        "top_artists": get_top_artists(user),
        "top_genres": []
    })
    os.remove(".cache"); os.remove(".cache-"+user)
    with open("data/database.json", "w") as file:
        json.dump(f, file)
    with open("data/database.json", "r") as f:
        f = json.load(f)
    for i in f:
        if i["name"] == user:
            top_genres = i["top_genres"]
            get_genres_top = get_favourite_genres(user)
            for j in get_genres_top:
                top_genres.append(j)
            i["top_genres"] = top_genres
    with open("data/database.json", "w") as file:
        json.dump(f, file)
    


