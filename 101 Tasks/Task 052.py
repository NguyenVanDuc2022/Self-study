"""
Question 052 - Level 02
Define a class named Rectangle which can be constructed by a length and width. The rectangle class has a method which
can compute the area.
Hints: Use def methodName(self) to define a method.
--- Nguyen Van Duc ---
"""


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


aRectangle = Rectangle(2, 10)
print(aRectangle.area())
