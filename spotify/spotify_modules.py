import spotipy, json
from secrets import client_secret, client_id
import numpy as np
import pandas as pd

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def save_csv(user):
    playlists = sp.user_playlists(user)["items"]
    print(f"{user}'s playlists:")
    playlist_ids = []
    x = 1

    for i in playlists:
        print(f"   {x}. "+i["name"]); x += 1
        playlist_ids.append(i["id"])
    wanted_pl = input("Enter number of wanted playlist: ")

    pl_id = playlist_ids[int(wanted_pl)-1]
    get_tracks = sp.playlist_items(pl_id)["items"]
    tracks = []
    track_ids = []
    for i in get_tracks:
        tracks.append(i["track"]["name"])
        track_ids.append(i["track"]["id"])

    features = sp.audio_features(track_ids)
    df = pd.DataFrame(features)
    names = []
    for i in range(len(df.index)):
        names.append("Noel")
    df["names"] = names

    df.to_csv(f"spotify/data/{pl_id}.csv")
    with open(f"spotify/data/{pl_id}.json", "w") as j: j.write(json.dumps(features, indent=4))
        
#print(sp.user_playlists("xfazze")["items"][1]["name"])
print(sp.track("46OSr5A12abROSe3rZXVSh")["name"])

