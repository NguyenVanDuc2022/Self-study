""" Calculator
----------------------------------------
"""


def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def subtraction():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 0
    while n != 0:
        ans = ans - n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0  # Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def average():
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]


# main...
while True:
    list1 = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list1 = addition()
            print("Ans = ", list1[0], " total inputs ", list1[1])
        elif c == 's':
            list1 = subtraction()
            print("Ans = ", list1[0], " total inputs ", list1[1])
        elif c == 'm':
            list1 = multiplication()
            print("Ans = ", list1[0], " total inputs ", list1[1])
        elif c == 'v':
            list1 = average()
            print("Ans = ", list1[0], " total inputs ", list1[1])
        else:
            print("Sorry, invilid character")
    else:
        break
