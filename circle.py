import math

def area(r: float) -> float:
    '''
    Return area of circle.

    Pararmeters:
    ------------
        r (float): radius of a circle.

    Return:
    -------
        area (float): area of a circle.

    Eximples:
    ---------
        >>> area(5)
        78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r: float) -> float:
    '''
    Return perimeter of circle.

    Pararmeters:
    ------------
        r (float): radius of a circle.

    Return:
    -------
        perimeter (float): perimeter of a circle.

    Eximples:
    ---------
        >>> perimeter(5)
        31.41592653589793
    '''
    return 2 * math.pi * r
print(perimeter(5))