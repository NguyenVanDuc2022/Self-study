"""
Question 01 - Level 01
Write a program which will find all such numbers which are divisible by 7 but are not multiple of 5, between 2000 and
3000 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hint:
Consider use range(#begin, #end) method
--- Nguyen Van Duc ---
"""

j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 == 0):
        j.append(str(i))
print(','.join(j))
