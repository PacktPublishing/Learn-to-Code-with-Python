# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects 
# whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True
def long_word(word):
    return len(word) > 7




# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False
def first_longer_than_second(string1, string2):
    return len(string1) > len(string2)
