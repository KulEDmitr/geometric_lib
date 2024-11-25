import math


def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Value must be number")
    if r < 0:
        raise ValueError("Value must be positive")
    return math.pi * r * r


def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Value must be number")
    if r < 0:
        raise ValueError("Value must be positive")
    return 2 * math.pi * r
