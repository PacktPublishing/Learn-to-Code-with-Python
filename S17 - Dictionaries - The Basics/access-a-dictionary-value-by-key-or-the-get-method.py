flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices["Seattle"])
# print(flight_prices["chicago"])

gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
}

print(gym_membership_packages[49])
print(gym_membership_packages[79])
# print(gym_membership_packages[100])

print(gym_membership_packages.get(29, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100))