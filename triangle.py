def area(a : int, h : int):
    '''
    Принимает числа a и h, возвращает площадь треугольника со сторонами a и h

    >>> area(3, 4)
    6
    '''
    return a * h / 2


def perimeter(a : int, b : int, c : int):    
    '''
    Принимает числа a, b и c, возвращает периметр треугольника со сторонами a, b и c

    >>> perimeter(3, 4, 5)
    12
    '''
    return a + b + c
