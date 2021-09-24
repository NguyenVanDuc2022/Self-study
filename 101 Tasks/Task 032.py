"""
Question 032 - Level 02
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values
are square of the keys.
Hints: Use dict[key] = value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
--- Nguyen Van Duc ---
"""


def printDict():
    d = dict()
    for i in range(0, 4):
        d[i] = i ** 2
    print(d)


printDict()
