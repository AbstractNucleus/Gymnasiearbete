import json
from collections import Counter
import operator

def get_favourite_genre(user, favourite_genre = ""):
    with open("database.json", "r") as f:
        f = json.load(f)
    for i in f:
        if user != i["name"]:
            print("User not found")
            exit()
        else:
            user_data = i
    genres = []
    for artist in user_data["top_artists"]:
        for genre in artist["genres"]:
            genres.append(genre)
    count = dict(Counter(genres))
    return max(count.items(), key=operator.itemgetter(1))[0]
    