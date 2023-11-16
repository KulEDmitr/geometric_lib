import math


def area(r):
    '''
    Принимает радиус, возвращает площадь круга
    Пример вызова:
    area(10) -> 314
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус, возвращает периметр круга
    Пример вызова:
    perimeter(10) -> 62.8
    '''
    return 2 * math.pi * r

