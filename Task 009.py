"""
Write a program and print the value according to the given formula: Q = sqrt([(2 * C * D)/H]) (in words: Q is equal to
the square root of [(2 times C times D) divided by H]. With a fixed value of C of 50, H of 30. D is a range of custom
values, entered from the user interface, the values of D are separated by commas.
For example:
Assuming the values string of D input is 100, 150 , 180, the output will be 18, 22, 24.
Suggestions:
If the output received is a decimal number, you need to round to the nearest values, for example 26.0 will be printed
as 26. In the case of input data provided to the question, it is assumed to be user input from the console.
"""

import math

c = 50
h = 30
values = []
items = [x for x in input("Input the values of d: ").split(",")]
for d in items:
    values.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))

print(",".join(values))
