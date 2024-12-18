import math

def area(r):
    """
    Вычисляет площадь окружности.

    Параметры:
        r (float): Радиус окружности.

    Возвращает:
        float: Площадь окружности.

    Пример вызова:
        >>> area(1)
        3.141592653589793
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности.

    Параметры:
        r (float): Радиус окружности.

    Возвращает:
        float: Длина окружности.

    Пример вызова:
        >>> perimeter(1)
        6.283185307179586
    """
    return 2 * math.pi * r
