# Declare a PizzaPie class that accepts a total_slices parameter. 
# In the instantiation process for an object, assign the parameter to an 
# attribute with the same name. 

# A PizzaPie object should also be initialized with a _slices_eaten 
# protected attribute set to 0.

class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    @property
    def slices_eaten(self):
        return self._slices_eaten

    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten <= self.total_slices:
            self._slices_eaten = slices_eaten

    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices

# Define a slices_eaten property. 
# The getter method should retrieve the value of the _slices_eaten attribute. 
# The setter method should set a new value for the _slices_eaten attribute
# but only if the argument is less than total_slices.

# Define a percentage property that calculates how much of the pie has been eaten 
# (the number of slices eaten divided by the total slices available). 
# The percentage property should be read-only.

# See sample execution below
#
cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage) # 0.25

cheese.slices_eaten = 4
print(cheese.percentage) # 0.5

cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
print(cheese.percentage) # 0.5
#
# ERROR - AttributeError: can't set attribute
# cheese.percentage = 0.50