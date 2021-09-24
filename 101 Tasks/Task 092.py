"""
Question 092 - Level 03
Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the ouput of the program should be:
ris etov ot esir
Hints: Use list[::-1] to iterate a list in a reverse order.
--- Nguyen Van Duc ---
"""
s = input("Enter your string: ")
s = s[::-1]
print(s)
