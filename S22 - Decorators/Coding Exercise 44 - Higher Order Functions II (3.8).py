# Define an "outer" function that accepts no arguments
# Inside the body of "outer", define an "inner" function
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function

def outer():
    def inner():
        return 5

    return inner

# print(outer()())