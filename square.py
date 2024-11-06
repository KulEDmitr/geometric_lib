def area(a: int): 
    '''
    Takes a number a and returns the area of a square with side a.
    The side length a must be a positive number.

    >>> area(3)
    9
    >>> area(5)
    25
    >>> area(10)
    100
    '''
    if a <= 0:
        raise ValueError("The side length of the square must be a positive number.")
    return a * a


def perimeter(a: int):
    '''
    Takes a number a and returns the perimeter of a square with side a.
    The side length a must be a positive number.

    >>> perimeter(3)
    12
    >>> perimeter(5)
    20
    >>> perimeter(10)
    40
    '''
    if a <= 0:
        raise ValueError("The side length of the square must be a positive number.")
    return 4 * a
