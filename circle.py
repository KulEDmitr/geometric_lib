import math


def area(r):
    '''Accepts number r - radius of circle,
    returns area of a circle of given radius.
        Example: area(3) -> 28.2743338823'''
    return math.pi * r * r


def perimeter(r):
    '''Accepts number r - the radius of the circle,
    returns the length of the circle of radius r.
        Example: perimeter(3) -> 18.8495559215'''
    return 2 * math.pi * r
