import math


def area(r):
    """
    Принимает радиус, возвращает площадь круга

    Параметр:
        r (int): радиус
    Возвращаемое значачение:
        math.pi * r * r (float): площадь круга

    Примеры:
        area(3) --> 9pi
        area(2) --> 4pi
    """

    return math.pi * r * r


def perimeter(r):
    """
    Принимает радиус, возвращает периметр круга

    Параметр:
        r (int): радиус
    Возвращаемое значение:
        2 * math.pi * r (float): периметр круга

    Примеры:
        perimeter(3) --> 6pi
        perimeter(2) --> 4pi
    """

    return 2 * math.pi * r

