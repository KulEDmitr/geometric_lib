import math

def area_circle(r):
    '''
    Вычисляет площадь окружности по радиусу.

    Параметры:
        r (int/float): радиус окружности

    Возвращаемое значение:
        float: площадь окружности

    Пример вызова:
        area_circle(5) -> 78.53981633974483
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    if r > 1_000_000:
        raise ValueError("Radius is too large")
    return math.pi * r * r


def perimeter_circle(r):
    '''
    Вычисляет периметр (длину) окружности по радиусу.

    Параметры:
        r (int/float): радиус окружности

    Возвращаемое значение:
        float: длина окружности

    Пример вызова:
        perimeter_circle(5) -> 31.41592653589793
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    if r > 1_000_000:
        raise ValueError("Radius is too large")
    return 2 * math.pi * r
