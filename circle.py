import math


def area(r):
    '''
    Принимает радиус окружности - r
    Возвращает площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Принимает радиус окружности - r
        Возвращает периметр окружности
    '''
    return 2 * math.pi * r

print(perimeter(25))