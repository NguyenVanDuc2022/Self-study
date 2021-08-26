"""
Write a program that accepts a comma-separated string of numbers from the console, produces a list and a tuple
containing all the numbers.
Example: Input given is 34, 67, 55, 33, 12, 98 then output is:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Suggestions:
Write a command that requires input of values and then use the data type conversion rule to complete
--- Nguyen Van Duc ---
"""
values = input("Enter the values: ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)