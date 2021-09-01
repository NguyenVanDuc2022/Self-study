"""
Question 041 - Level 02
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half
values in one line.
Hints:
Use [n1:n2] notation to get a slice from a tuple.
--- Nguyen Van Duc ---
"""
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ltp = int(len(tp)/2)
print(tp[:ltp])
print(tp[ltp:])
