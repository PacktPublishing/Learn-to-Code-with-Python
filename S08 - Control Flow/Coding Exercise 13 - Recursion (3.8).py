# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120

# 5!
# 5 * 4!
# 5 * 4 * 3!
# 5 * 4 * 3 * 2!
# 5 * 4 * 3 * 2 * 1!


def factorial(number):
    if number == 1:
        return number

    return number * factorial(number - 1)

print(factorial(5))