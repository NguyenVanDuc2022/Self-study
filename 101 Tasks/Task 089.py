"""
Question 089 - Level 03
With a given list [12,224,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate
values with original order reserved.
Hints: Use set() to store a number of values without duplicate.
--- Nguyen Van Duc ---
"""


def removeDuplicate(li):
    newli = []
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    return newli


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicate(li))
