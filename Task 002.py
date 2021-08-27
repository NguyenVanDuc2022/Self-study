"""
Write a program that can calculate the factorial of a given number. Results are printed as a string on one line,
separated by commas. For example, the given number is 8 then the output should be 40320.

Suggestions: In the case of input data provided, you choose how to have the user enter the number.
--- Nguyen Van Duc ---
"""

x = int(input("Enter the number to calculate the factorial: "))


def fact(y):
    if y == 1:
        return 1
    return y * fact(y - 1)


print(fact(x))
