import math

'''Подключем библиотеку math'''


def area(r):
    
    '''Функция принимает r <- радиус круга. Возвращает его площадь'''

    return math.pi * r * r
    ''' area(3) ; return 9*3,14'''


def perimeter(r):
    
    '''Функция принимает r <- радиус круга. Возвращает длину его окружности'''
    
    return 2 * math.pi * r
    ''' perimeter(3) ; return 6*3,14 '''