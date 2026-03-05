# Declare a set with 3 of your favorite movies as strings.
# Assign it to a movies variable.
movies = { "Commando", "Die Hard", "Memento" }

# Declare a set with the first four months of the year as strings.
# Assign it to a months variable.
months = { "January", "February", "March", "April" }


# Create an empty set and assign it to an empty variable.
empty = set()


# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#
# EXAMPLES:
# remove_duplicates([1, 2, 1, 2])  => [1, 2] or [2, 1]
# remove_duplicates([1, 2, 3, 4])  => [1, 2, 3, 4] in some order

def remove_duplicates(elements):
    return list(set(elements))