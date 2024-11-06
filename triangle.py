def area(a: int, h: int):
    '''
    Takes numbers a and h, and returns the area of a triangle with base a and height h.
    Both a and h must be positive numbers.

    >>> area(3, 4)
    6
    '''
    if a <= 0 or h <= 0:
        raise ValueError("The base and height of the triangle must be positive numbers.")
    return a * h / 2


def perimeter(a: int, b: int, c: int):    
    '''
    Takes numbers a, b, and c, and returns the perimeter of a triangle with sides a, b, and c.
    All sides must be positive numbers.

    >>> perimeter(3, 4, 5)
    12
    '''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides of the triangle must be positive numbers.")
    return a + b + c
