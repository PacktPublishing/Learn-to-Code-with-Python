employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

*names, position, age = employee
print(position)
print(age)
print(names)

first_name, *details, age = employee
print(first_name)
print(age)
print(details)

first_name, last_name, position, *details = employee
print(details)