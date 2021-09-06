"""
Question 100 - Level 03
Matrix Transpose using Nested List Comprehension
--- Nguyen Van Duc ---
"""

X = [[12, 7],
     [4, 5],
     [3, 8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
    print(r)
