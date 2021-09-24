"""
Question 044 - Level 02
Write a program which can filter even number in a list using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
Hints:
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
--- Nguyen Van Duc ---
"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda x: x % 2 == 0, li))
print(evenNumbers)
