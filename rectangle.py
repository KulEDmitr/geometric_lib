def area(a: float, b: float) -> float:
    """
    Возвращает площадь прямоугольника со сторонами a, b

        :param a: длина прямоугольника
        :type a: float
        :param b: ширина прямоугольника
        :type b: float
        :returns: периметр прямоугольника
        :rtype: float

    Пример вызова:
        s = area(5, 2)  # В s запишется 10
    """
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")
    return a * b 


def perimeter(a: float, b: float) -> float:
    """
    Возвращает периметр прямоугольника со сторонами a, b

        :param a: длина прямоугольника
        :type a: float
        :param b: ширина прямоугольника
        :type b: float
        :returns: периметр прямоугольника
        :rtype: float

    Пример вызова:
        p = perimeter(5, 2)  # В p запишется 14
    """
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")
    return 2 * (a + b)
