"""
Question 028 - Level 01
Define a function that can receive two integral numbers in string form and compute their sum and then print it in
console.
Hints: use int() to convert a string to integer.
--- Nguyen Van Duc ---
"""


def printValue(s1, s2):
    print ("%s + %s = %d" %(s1,s2,int(s1) + int(s2)))


printValue("3", "4")