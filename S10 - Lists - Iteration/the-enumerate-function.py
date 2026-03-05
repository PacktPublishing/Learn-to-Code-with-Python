errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for idx, task in enumerate(errands, 1):
    print(f"{task} is number {idx} on my list of things to do today!")