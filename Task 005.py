"""
Define a class with at least 2 methods:
getString: to get a user inputted string from the console.
printString: print the string entered to upper case.
Add simple checker functions to test class methods.

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
