"""
Question 025 - Level 01
Define a class, which have a class parameter and have a sam instance parameter.
Hints:  Define a instance parameter, need add it in __init__ method.
        You cna init a object with construct parameter or set the value later.
--- Nguyen Van Duc ---
"""


class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
print("%s name is %s" % (Person.name, nico.name))
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
