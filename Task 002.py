"""
Question 02 - Level 01
Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated
sequence on a single line. Suppose the following input is supplied to the program.
8
Then, the output should be:
40320
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
--- Nguyen Van Duc ---
"""


def fact(y):
    if y == 1:
        return 1
    return y * fact(y - 1)


x = int(input("Enter the number to calculate the factorial: "))
print(fact(x))
