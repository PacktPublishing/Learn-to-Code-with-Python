film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors)

# film_directors.setdefault("Bad Boys")
# print(film_directors)

film_directors.setdefault("Bad Boys", "Michael Bay")
print(film_directors)

film_directors.setdefault("Bad Boys", "A good director")
print(film_directors)