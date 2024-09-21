"""
This file has a lot of math functions in it
"""

def factorial(num) -> int:
    """
    Factorial a number
    """
    result = 1
    if num == 0 or num == 1:
        return result
    elif num <= 0:
        return None
    else:
        for x in range(2, num + 1):
            result *= x
        return result

def power(num, power) -> int:
    return num ** power