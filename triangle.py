import unittest


def area(a, h):
    '''
    Вычисляет площадь треугольника.

    Args:
        a (float): Длина основания треугольника.
        h (float): Длина высоты, опущенной к основанию.

    Returns:
        float: Площадь треугольника.

    Пример использования:
    import triangle
    base = 6
    height = 4
    area_result = triangle.area(base, height)
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Вычисляет периметр треугольника.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.

    Пример использования:
    import triangle
    side1 = 3
    side2 = 4
    side3 = 5
    perimeter_result = triangle.perimeter(side1, side2, side3)
    '''
    return a + b + c


