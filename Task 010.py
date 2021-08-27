"""
Write a program that takes 2 digits X,Y takes the values from the input and creates a 2 dimensional array. The element
value in the i-th row and j-th column of the array must be i*j.
Note: i = 0, 1, ..., X-1; j = 0, 1, ..., Y-1.
For example: Input X, Y value is 3,5, the output is: [[0, 0, 0, 0, 0],[0, 1, 2, 3, 4],[0, 2, 4, 6, 8]]
Suggestions: Write a command to get X,Y values from the console inputted by the user.
"""
input_str = input("Enter X, Y: ")
dimensions = [int(x) for x in input_str.split(",")]
rowNum = dimensions[0]
colNum = dimensions[1]
multi_list = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multi_list[row][col] = row * col

print(multi_list)
