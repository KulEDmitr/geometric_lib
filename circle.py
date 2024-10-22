import math

def area(r):
    '''
    Принимает число r, возвращает площадь окружности с радиусом r
    Пример вызова:
    r = 5
    result = area(r)
    print(result)
    Вывод: 78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает периметр окружности с радиусом r
    Пример вызова:
    r = 5
    result = perimeter(r)
    print(result)
    Вывод: 31.41592653589793
    '''
    return 2 * math.pi * r
