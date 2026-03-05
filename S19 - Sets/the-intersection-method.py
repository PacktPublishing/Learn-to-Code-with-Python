candy_bars = { "Milky Way", "Snickers", "100 Grand" }
sweet_things = { "Sour Patch Kids", "Reeses Pieces", "Snickers" }

print(candy_bars.intersection(sweet_things))
print(candy_bars & sweet_things)

values = { 3.0, 4.0, 5.0 }
more_values = { 3, 4, 5, 6 }
print(values.intersection(more_values))
print(more_values.intersection(values))
print(values & more_values)
print(more_values & values)