import math


def area(r):
    """
    Return the area of the circle.

    Args:
        r (int): circle radius.

    Example:
        area(5) --> 78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """
    Return the perimeter of the circle.

    Args:
        r (int): circle radius.

    Example:
        perimeter(5) --> 31.41592653589793
    """
    return 2 * math.pi * r

