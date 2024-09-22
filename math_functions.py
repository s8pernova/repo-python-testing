"""
This file has a lot of math functions in it
"""

numbers = [50, 2, 3, 43, 89]

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
        for i in range(2, num + 1):
            result *= i
        return result

<<<<<<< HEAD
def average(list) -> float:
    """
    Find the average in a list of numbers
    """
    sum = 0
    for i in range(len(list)):
        sum += list[i - 1]
    
    return sum / len(list)

print(average(numbers))
=======
def find_slope(x1, y1, x2, y2) -> float:
    """
    Find the slope of two points
    """
    return (y2 - y1) / (x2 - x1)
>>>>>>> a0018f205aed3870a60341bf705b5344bac4b4ae
