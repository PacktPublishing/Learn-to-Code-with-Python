# Given the great_directors list below, overwrite the “Steven Spielberg” 
# string with a string of “Michael Bay”.
great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
great_directors[1] = "Michael Bay"


# Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
transformers[2] = "Grimlock"


# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]
camping_trip_supplies[0] = "Food"


# Given the tech_companies list below, overwrite the Microsoft, Blackberry, and IBM strings 
# with the strings “Facebook” and “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]

tech_companies[1:4] = ["Facebook", "Apple"]
print(tech_companies)