"""
Question 031 - Level 02
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
otherwise print "It is an odd number".
Hints: Use % operator to check if a number is even or odd.
--- Nguyen Van Duc ---
"""


def checkValue(number):
    if number % 2 == 0:
        print("It is an even number!")
    else:
        print("It is an odd number!")


checkValue(15)
