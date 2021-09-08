"""
Question 102 - Level 03
Matrix multiplication Using Nested List Comprehension
--- Nguyen Van Duc ---
"""
# Program to multiply two matrices using list comprehension
# 3x3 matrix
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
# 3x4 matrix
Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
# result in 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
     print(r)
