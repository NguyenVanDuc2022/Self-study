"""
Question 073 - Level 03
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random
module and comprehension.
Hints: Use random.choice() to random element from a list.
--- Nguyen Van Duc ---
"""
import random

print(random.choice([i for i in range(201) if i % 5 == 0 and i % 7 == 0]))
