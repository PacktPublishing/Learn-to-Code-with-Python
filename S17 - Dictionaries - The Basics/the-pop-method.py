# years = [1991, 1995, 2000, 2007]
# years.pop(1)
# print(years)

release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

# year = release_dates.pop("Java")
# print(release_dates)
# print(year)

# release_dates.pop("Go")
# print(release_dates)

# if "Rust" in release_dates:
#     release_dates.pop("Rust")

# new_year = release_dates.pop("Ruby", 2000)
# print(new_year)

del release_dates["Java"]
print(release_dates)

del release_dates["Rust"]