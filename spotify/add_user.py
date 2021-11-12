from spotify_database_modules import get_50_recent_songs, get_50_top_artists, get_playlists
import json

def save_user_data(user):
    with open("database.json", "r") as f:
        f = json.load(f)
    for i in f:
        if i["name"] == user:
            print("User has already been added")
            exit()
    f.append({
        "name": user,
        "playlists": get_playlists(user),
        "recently_played": get_50_recent_songs(user),
        "top_artists": get_50_top_artists(user)
    })
    with open("database.json", "w") as file:
        json.dump(f, file)



save_user_data("1195493091")
# Remove .cache files and logout from browser




'''
with open("user_data.json", "r") as f:
    f = json.load(f)
    for i in f:
        print(i["name"])
        for j in i["top_artists"]:
            print("    ", j["name"])
'''