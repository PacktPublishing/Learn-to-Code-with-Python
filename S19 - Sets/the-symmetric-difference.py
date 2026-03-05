candy_bars = { "Milky Way", "Snickers", "100 Grand" }
sweet_things = { "Sour Patch Kids", "Reeses Pieces", "Snickers" }

print(candy_bars.symmetric_difference(sweet_things))
print(candy_bars ^ sweet_things)

print(sweet_things.symmetric_difference(candy_bars))
print(sweet_things ^ candy_bars)