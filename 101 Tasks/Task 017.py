"""
Question 017 - Level 02
Write a program that computes the net amount of a bank based a transaction log from console input. The transaction log
format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
--- Nguyen Van Duc ---
"""
netAmount = 0
while True:
    s = input("Enter values: ")
    if not s:
        break
    values = s.split(" ")
    if values[0] == "D":
        netAmount += int(values[1])
    elif values[0] == "W":
        netAmount -= int(values[1])
    else:
        pass
    print("netAmount is:", netAmount)

print("The final netAmount is:", netAmount)
