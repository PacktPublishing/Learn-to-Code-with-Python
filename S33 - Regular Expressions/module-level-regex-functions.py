import re

print(re.search("flower", "Picking flowers in the flower field"))

print(re.match("flower", "flower field"))

print(re.findall("flower", "Picking flowers in the flower field"))

for match in re.finditer("flower", "Picking flowers in the flower field"):
    print(match)