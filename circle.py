import math


def area(r):
    """
    Возвращает площадь окружности на основе переданного ему радиуса.
        param: a (int|float) - радиус окружности;
    return: square (float) - площадь квадрата.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр окружности на основе переданного ему радиуса.
        param: a (int|float) - радиус окружности;
    return: square (float) - площадь квадрата.
    """
    return 2 * math.pi * r

