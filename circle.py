import math


def area(r):
    """Принимает радиус окружности (int)
        возвращает её площадь (float)

        print(area(10)) --> 314.1592653589793"""
    return math.pi * r * r


def perimeter(r):
    """Принимает радиус окружности (int)
        возвращает её периметр (float)

        print(perimeter(10)) --> 62.83185307179586"""
    return 2 * math.pi * r
