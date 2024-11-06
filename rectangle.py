def area(a: int, b: int):
    '''
    Takes numbers a and b, returns the area of a rectangle with sides a and b.
    Both a and b must be positive numbers.

    >>> area(3, 4)
    12
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Rectangle sides must be positive numbers.")
    return a * b


def perimeter(a: int, b: int):
    '''
    Takes numbers a and b, returns the perimeter of a rectangle with sides a and b.
    Both a and b must be positive numbers.

    >>> perimeter(3, 4)
    14
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Rectangle sides must be positive numbers.")
    return 2 * (a + b)
