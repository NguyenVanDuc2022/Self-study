"""
Question 024 - Level 01
Python has many built-in functions, and if you do now know how to use it, you can read document online or find some
books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), input()
Hints: The built-in document method is __doc__
--- Nguyen Van Duc ---
"""
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    """
    Return the square value of the input number.
    The input number must be integer.
    """
    return num ** 2


print("Square(2) =", square(2))
print(square.__doc__)
