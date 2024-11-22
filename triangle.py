def area(a: float, h: float) -> float:
    '''
    Return area of triangle.

    Pararmeters:
    ------------
        a (float): first number.
        b (float): second number.

    Return:
    -------
        area (float): area of a triangle with side `a` and height `b`.

    Eximples:
    ---------
        >>> area(1, 2)
        1
    '''
    return a * h / 2

def perimeter(a: float, b: float, c: float) -> float:
    '''
    Return perimeter of triangle.

    Pararmeters:
    ------------
        a (float): first number.
        b (float): second number.
        c (float): third number.

    Return:
    -------
        perimeter (float): perimeter of a triangle with sides `a`, `b` and `c`.

    Eximples:
    ---------
        >>> perimeter(1, 2, 3)
        6
    '''
    return a + b + c
