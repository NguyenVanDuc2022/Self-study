"""
Question 055 - Level 02
Write a function to compute 5/0 and use try/except to catch the exceptions.
Hints: Use try/except to catch exceptions.
--- Nguyen Van Duc ---
"""
def throw():
    return 5/0

try:
    throw()
except ZeroDivisionError:
    print("Division by zero!")
except Exception:
    print("Caught an exception.")
finally:
    print("In finally block for cleanup!")