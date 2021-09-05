"""
Question 091 - Level 03
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program.
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,2
f,1
Hints:
Use dict to store key/values pairs.
Use dict.get() method to lookup a key with default value.
--- Nguyen Van Duc ---
"""
dic = {}
s = input("Enter your string: ")
for c in s:
    dic[c] = dic.get(c, 0) + 1
print('\n'.join(['%s, %s' % (k, v) for k, v in dic.items()]))
