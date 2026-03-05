tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Scary Monster", "Scary Alien"],
            "Genre": "Science Fiction",
            "Year": 1993
        },
        "Season 2": {
            "Episodes": ["Scary Conspiracy"],
            "Genre": "Horror",
            "Year": 1994
        }
    },
    "Lost": {
        "Season 1": {
            "Episodes": ["What The Heck Is Happening On This Island?"],
            "Genre": "Science Fiction",
            "Year": 2004
        }
    }
}

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["The X-Files"]["Season 2"]["Year"])
print(tv_shows["Lost"]["Season 1"]["Genre"])
