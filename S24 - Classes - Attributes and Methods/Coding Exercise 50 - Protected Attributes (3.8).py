# Let’s say we want to model a Book as a Python object. 
# A Book has an author and a publisher, which are characteristics that cannot change. 
# A Book also has a page_count, which could be altered if you rip some pages from the book.

# Declare a Book class that accepts author, publisher, and page_count parameters. 
# Each of the parameters should be assigned to an attribute. 
# The author and publisher attributes should be designated as protected (use an underscore). 
# The page_count attribute should be designated public.

class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

    def copyright(self):
        return f"Copyright {self._author}, {self._publisher}"

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0

# Define a copyright instance method that returns a string with information about the copyright. 
# It should look the string below, where “Grant Cardone” is the value of the protected
# author attribute and “10X Enterprises” is the value of the protected publisher attribute.

# => Copyright Grant Cardone, 10X Enterprises

# The public page_count attribute can always be manually modified. 
# However, we can still define an instance method that modifies it. 

# Declare a rip_in_half instance method. 
# If the book has more than 1 page, it should halve the page_count. 
# If the book has 1 page or less, it should set the page_count to 0.

# See sample execution below

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0