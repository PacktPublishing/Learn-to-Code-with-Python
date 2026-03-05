concert_attendees = [
    { "name": "Taylor", "section": 400, "price paid": 99.99 },
    { "name": "Christina", "section": 200, "price paid": 149.99 },
    { "name": "Jeremy", "section": 100, "price paid": 0.0 }
]

for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}.")