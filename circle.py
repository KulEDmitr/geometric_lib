import math


def area(r):
    '''Принимает на вход радиус круга r, возвращает площадь круга
    Пример: area = circle.area(4) #Output: 50.26548245743669'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает на вход радиус круга r, возвращает периметр круга
    Пример: per = circle.perimeter(4) #Output: 25.132741228718345'''
    return 2 * math.pi * r