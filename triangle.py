def area(a, h):
    '''Принимает значение стороны и высоты и выводит площадь треугольника
    >>> area(3, 4)
        6.0
    '''
    if a < 0 or h < 0:
        return 0
    return a * h / 2 

def perimeter(a, b, c):
    '''Принимает значение сторон и выводит периметр треугольника
    >>> perimeter(3, 5, 5)
        13
    '''
    if a < 0 or b < 0 or c < 0:
        return 0
    return a + b + c



