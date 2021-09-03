"""
Question 076 - Level 03
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, between 1 and 1000
inclusive.
Hints: Use random.samples() to generate a list of random values.
--- Nguyen Van Duc ---
"""
import random

print(random.sample([i for i in range(1, 10001) if i % 5 == 0 and i % 7 == 0], 5))
