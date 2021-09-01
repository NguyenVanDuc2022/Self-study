"""
Question 043 - Level 02
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
print "No"
Hints: Use if statement to judge condition.
--- NGuyen Van Duc ---
"""
s = input("Enter your value: ")
if s.upper() == "YES":
    print("Yes")
else:
    print("No")