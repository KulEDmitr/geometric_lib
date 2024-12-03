def area(a):
    '''
    Принимает значение стороны и выводит площадь квадрата
    >>> area(3)
        9
    '''
    if a < 0:
        return 0
    return a * a

def perimeter(a):
    '''Принимает значение стороны и выводит периметр квадрата
    >>> perimeter(3)
        12
    '''
    if a < 0:
        return 0
    return 4 * a
