import math

def area(r):
    '''
    Counts the area of the circle, using radius
    Parameters:
        r -- radius of the circle (int or float)
    Return value:
        float -- S of the circle
    Example:
        print(area(3)) // prints the area (=28.27433) of the circle with radius 3
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Counts the perimeter of the circle, using radius
    Parameters:
        r -- radius of the circle (int or float)
    Return value:
        float -- P of the circle
    Example:
        print(perimeter(3)) // prints the perimeter (=18.84956) of the circle with radius 3
    '''
    return 2 * math.pi * r

