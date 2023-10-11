import math

def area(r):
    '''Принимает число r, возвращает площадь окружности радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает периметр окружности радиусом r'''
    return 2 * math.pi * r
print (perimeter(6))
