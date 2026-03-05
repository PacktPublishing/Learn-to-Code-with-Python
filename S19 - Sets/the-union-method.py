candy_bars = { "Milky Way", "Snickers", "100 Grand" }
sweet_things = { "Sour Patch Kids", "Reeses Pieces", "Snickers" }

print(candy_bars.union(sweet_things))
print(sweet_things.union(candy_bars))

print(candy_bars | sweet_things)
print(sweet_things | candy_bars)