import math


def area(r):
    """ Возвращает площадь круга
            Параметры:
                r (int): радиус круга
            Возвращаемое значение:
                area (int): площадь круга
    Пример вызова:
        area(2) -> 4*(pi)
    """
    return math.pi * r * r


def perimeter(r):
    """ Возвращает периметр круга
            Параметры:
                a (int): радиус круга
            Возвращаемое значение:
                perimeter (int): периметр круга
    Пример вызова:
        perimeter(2) -> 4*(pi)
    """
    return 2 * math.pi * r

