def area(a, b):
    '''Принимает значение сторон и выводит площадь прямоугольника
    >>> area(3, 4)
        12
    '''
    if a < 0 or b < 0:
        return 0
    return a * b 

def perimeter(a, b):
    '''Принимает значение сторон и выводит периметр прямоугольника
    >>> perimeter(3, 4)
    14
    '''
    if a < 0 or b < 0:
        return 0
    return 2 * (a + b)

