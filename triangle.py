def area(a, h): 
    """
    Вычисляет площадь треугольника.

    Параметры:
        a (float): Длина основания треугольника.
        h (float): Высота треугольника, проведенная к основанию.

    Возвращает:
        float: Площадь треугольника.

    Пример вызова:
        >>> area(3, 4)
        6.0
    """
    return a * h / 2 


def perimeter(a, b, c): 
    """
    Вычисляет периметр треугольника.

    Параметры:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Возвращает:
        float: Периметр треугольника.

    Пример вызова:
        >>> perimeter(3, 4, 5)
        12
    """
    return a + b + c
