"""
Question 05 - Level 01
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case
Also please include simple test function to test the class methods.
Hints: Use __init__ method to construct some parameters
For example: The input string is nguyenvanduc.ds, the output must be NGUYENVANDUC.DS
--- Nguyen Van Duc ---
"""


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter string: ")

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()
