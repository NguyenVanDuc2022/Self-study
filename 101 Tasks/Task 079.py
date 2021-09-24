"""
Question 079 - Level 03
Please write a program to print the running time of execution of "1+1" for 100 times.
Hints: Use timeit() function to measure the running time.
--- Nguyen Van Duc ---
"""
from timeit import Timer

t = Timer("for i in range(100): 1 + 1")
print(t.timeit())
