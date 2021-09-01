"""
Question 049 - Level 02
Define a class named American which has a static method called printNationally.
Hints: Use @staticmethod decorator to define class static method.
--- Nguyen Van Duc ---
"""


class American(object):
    @staticmethod
    def printNationally():
        print("America")


anAmerica = American()
anAmerica.printNationally()
American.printNationally()
