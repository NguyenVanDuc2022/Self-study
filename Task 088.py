"""
Question 088 - Level 03
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are
intersection of the above given lists.
Hints: Use set() and "&=" to do set intersection operation.
--- Nguyen Van Duc ---
"""
set1 = {1, 3, 6, 78, 35, 55}
set2 = {12, 24, 35, 24, 88, 120, 155}
set1 &= set2
li = list(set1)
print(set1)
