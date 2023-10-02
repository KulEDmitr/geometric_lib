import math


def area(r):
    """
    Return the area of the circle.

    Args:
        r (int): circle radius.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Return the perimeter of the circle.

    Args:
        r (int): circle radius.
    """
    return 2 * math.pi * r


print(perimeter(5))
