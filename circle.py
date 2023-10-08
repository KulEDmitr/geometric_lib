import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            area (int): площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            perimeter (int): периметр круга
    '''
    return 2 * math.pi * r

