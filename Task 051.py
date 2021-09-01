"""
Question 051 - Level 02
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the
area.
Hints: Use def methodName(self) to define a method.
--- Nguyen Van Duc ---
"""


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def are(self):
        return self.radius ** 2 * 3.14


aCircle = Circle(2)
print(aCircle.are())
