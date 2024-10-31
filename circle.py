import math


def area(r: float) -> float:
    """
    Возвращает площадь круга с радиусом r

        :param r: радиус круга
        :type r: float
        :returns: площадь круга
        :rtype: float

    Пример вызова:
         s = area(2)  # В s запишется 12.56
    """
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает длину окружности с радиусом r

        :param r: радиус круга
        :type r: float
        :returns: длина окружности
        :rtype: float

    Пример вызова:
        p = perimeter(1)  # В p запишется 6.28
    """
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r
