def area(a : int):
    '''
    Принимает число a, возвращает площадь квадрата со стороной n

    >>> area(3)
    9
    >>> area(5)
    25
    >>> area(10)
    100
    '''
    return a * a


def perimeter(a : int):
    '''
    Принимает число a, возвращает периметр квадрата со стороной a

    >>> perimeter(3)
    12
    >>> perimeter(5)
    20
    >>> perimeter(10)
    40
    '''
    return 4 * a
