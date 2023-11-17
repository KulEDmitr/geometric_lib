import math


def area(r):

    '''Принимает число r, возвращает площадь окружности радиусом r

       Входное значение: 6
       Результат: 113.09733552923255

       Входное значение: -6
       Результат: Radius can't be negative
    '''

    if r < 0:
        raise ValueError("Radius can't be negative")

    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает периметр окружности радиусом r

       Входное значение: 6
       Результат: 37.69911184307752

       Входное значение: -6
       Результат: Radius can't be negative
    '''
    if r < 0:
        raise ValueError("Radius can't be negative")

    return 2 * math.pi * r

