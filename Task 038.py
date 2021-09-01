"""
Question 038 - Level 02
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function need to print the last 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list.
"""


def printList():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[-5:])


printList()
