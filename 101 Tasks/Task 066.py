"""
Question 066 - Level 02
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma
separated form while n is input by console.
Example: If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
Hints: Use yield to procedure the next value in generator.
In case of input data being supplied to the question, it should be assumed to be a console input.
--- Nguyen Van Duc ---
"""


def NumGenerator(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


n = int(input("Enter your number: "))
values = []
for i in NumGenerator(n):
    values.append(str(i))
print(",".join(values))
