def area_triangle(a, h):
    '''
    Вычисляет площадь треугольника исходя из его высоты и длины стороны, к которой проведена высота.

    Параметры:
        a (int/float): длина стороны
        h (int/float): высота

    Возвращаемое значение:
        float: площадь треугольника

    Пример вызова:
        area_triangle(5, 3) -> 7.5
    '''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Both base and height must be numbers")
    if a <= 0 or h <= 0:
        raise ValueError("Base and height must be positive values")
    if a > 1_000_000 or h > 1_000_000:
        raise ValueError("Base or height is too large")
    return a * h * 0.5


def perimeter_triangle(a, b, c):
    '''
    Вычисляет периметр треугольника исходя из длины его сторон.

    Параметры:
        a (int/float): длина стороны
        b (int/float): длина стороны
        c (int/float): длина стороны

    Возвращаемое значение:
        float: периметр треугольника

    Пример вызова:
        perimeter_triangle(5, 3, 4) -> 12
    '''
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All sides must be numbers")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive values")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle")
    if any(x > 1_000_000 for x in [a, b, c]):
        raise ValueError("One or more sides are too large")
    return a + b + c
