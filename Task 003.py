"""
Given a given integer n, write a program to generate a dictionary containing (i,i*i) as integers from 1 to n (including
1 and n) and then print this dictionary. Example: Assuming number n i 8, the output will be:
{1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}.
Suggestions:
Write a command that requires the input of an integer n.
--- Nguyen Van Duc ---
"""
n = int(input("Enter a number: "))
d = dict()
for i in range(1,n+1):
    d[i] = i*i


print(d)
