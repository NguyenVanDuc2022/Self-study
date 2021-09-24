"""
Question 057 - Level 02
Assuming that we have some email addresses in the "username@companyname.com" format, please write a program to print the
username of a given email address. Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints: Use \w to match letters.
--- Nguyen Van Duc ---
"""
import re

emailAddress = input("Enter your email: ")
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2, emailAddress)
print(r2.group(1))
print(r2.group(2))
