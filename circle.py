import math
import unittest


def area(r):
    '''
        Принимает радиус круга, возвращает его площадь
        area(r): площадь круга с радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Принимает радиус окружности, возвращает ее периметр
        perimeter(r): периметр окружности с радиусом r
    '''
    return 2 * math.pi * r

