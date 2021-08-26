"""
Defines a class that has a class parameter and the same instance parameter.

Suggestions:
When defining instance parameter, need to add it to __init__
You can initialize and object with a start parameter or set a value later.
--- Nguyen Van Duc ---
"""


class Person:
    # Define class name
    name = "Person"

    def __init__(self, name=None):
        # self.name is instance variable
        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
