"""
Python has many built-in function, if you don't know how to use it, you can read the documentation online or find some
books. But Python also has function documentations available for every built-in function in Python. The requirement of
this task is to write a program to print documentation of some of the built-in Python functions such asn abs(), int(),
input() and add documentation for the function you define yourself.

Suggestions: Utilize __doc__
--- Nguyen Van Duc ---
"""
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    """
    Returns the square of the number entered.
    The number entered must be integer.
    """
    return num ** 2


print(square.__doc__)
