import math


def area(r):
    """
    Вычисляет площадь круга.

    Параметры:
        r (float): радиус круга.

    Возвращаемое значение:
        (float): площадь круга.

    Пример использования:
        >>> circle.area(10)
        314.1592653589793
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")

    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")

    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга.

    Параметры:
        r (float): радиус круга.

    Возвращаемое значение:
        (float): периметр круга.

    Пример использования:
        >>> circle.perimeter(8)
        50.26548245743669
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")

    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")

    return 2 * math.pi * r

