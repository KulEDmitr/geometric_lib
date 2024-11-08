import math


def area(r):
    '''вычисляет площадь окружности по принимаемому числу r
    Пример: area(2) = pi*4
    '''
    return math.pi * r * r


def perimeter(r):
    '''вычисляет периметр окружности по принимаемому числу r
    Пример: perimetr(2) = 4*pi
    '''
    return 2 * math.pi * r