def area(a: int, h: int):
    """
    Принимает длину основания и высоту, возвращает площадь треугольника

    Параметры:
        a (int): длина основания
        h (int): высота
    Возвращаемое значение:
        a * h / 2 (float): площадь треугольника

    Примеры:
        area(3, 5) --> 7.5
        area(1, 2) --> 1.0
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")
    elif h <= 0:
        raise ValueError("height can't be negative or equal to zero")

    return a * h / 2


def perimeter(a, b, c):
    """
    Принимает длины 3-х сторон, возвращает периметр треугольника

    Параметры:
        a (int): длина 1 стороны
        b (int): длина 2 стороны
        c (int): длина 3 стороны
    Возвращаемое значение:
        a + b + c (int): периметр треугольника

    Примеры:
        perimeter(3, 5, 6) --> 14
        perimeter(1, 2, 3) --> 6
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")
    elif b <= 0:
        raise ValueError("length can't be negative or equal to zero")
    elif c <= 0:
        raise ValueError("length can't be negative or equal to zero")

    return a + b + c
