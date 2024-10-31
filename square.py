def area(a: float) -> float:
    """
    Возвращает площадь квадрата со стороной a

        :param a: длина стороны квадрата
        :type a: float
        :returns: площадь квадрата
        :rtype: float

    Пример вызова:
        s = area(5)  # В s запишется 25
    """
    if a < 0:
        raise ValueError("Side cannot be negative")
    return a * a


def perimeter(a: float) -> float:
    """
    Возвращает периметр квадрата со стороной a

        :param a: длина стороны квадрата
        :type a: float
        :returns: периметр квадрата
        :rtype: float

    Пример вызова:
        p = perimeter(5)  # В p запишется 20
    """
    if a < 0:
        raise ValueError("Side cannot be negative")
    return 4 * a
