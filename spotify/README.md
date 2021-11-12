# Example structure of database.json

## Contents of each item
```

[ i ] --> { "name", "playlists", "recently_played", "top_artists", "top_genres" }

    [ "playlists" ] --> [ { "name", "id", "songs" } ]

        [ "songs" ] [ i ] --> { "name", "artists"}

            [ "artists" ] [ i ] --> { "name", "id", "genres" }



    [ "recently_played" ] --> { "name", "artists" }

        [ "artists" ] [ i ] --> { "name", "id", "genres" }



    [ "top_artists" ] [ i ] --> { "name", "id", "genres" }

```

## Example item
```

[
    {
        "name": "weepur007",

        "playlists": [
            {
                "name": "Metal & Rock",
                "id": "g324hjgkg3",
                "songs": [
                    {
                        "name": "Contry Roads",
                        "artists": [
                            {
                                "name": "John Denver",
                                "id": "674sdf6dsf756",
                                "genres": [
                                    "country", 
                                    "techno", 
                                    "jazz", 
                                    "techno", 
                                    "techno"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],


        "recently_played" (*50): [
            {
                "name": "Contry Roads",
                "artists": [
                    {
                        "name": "John Denver",
                        "id": "674sdf6dsf756",
                        "genres": [
                            "country", 
                            "techno", 
                            "jazz", 
                            "techno", 
                            "techno"
                        ]
                    }
                ]
            }
        ],


        "top_artists" (*50): [
            {
                "name": "John Denver",
                "id": "674sdf6dsf756",
                "genres": [
                    "country", 
                    "techno", 
                    "jazz", 
                    "techno", 
                    "techno"
                ]
            }
        ],


        "top_genres" (*10): [
            "pop", 
            "swedish pop", 
            "rock", 
            "electropop", 
            "swedish hip hop", 
            "glitchcore", 
            "swedish idol pop", 
            "swedish pop rap", 
            "permanent wave", 
            "metal"
        ]
    }
]

```
