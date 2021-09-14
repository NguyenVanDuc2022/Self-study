"""
Question 10 - Level 02
Write a program that accepts a sequence of whit space separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set of container to remove duplicated data automatically and then use sorted() to sort the data.
--- Nguyen Van Duc ---
"""

s = input("Enter strings: ")
words = [word for word in s.split(" ")]
words = list(set(words))
words.sort()
print(" ".join(words))
