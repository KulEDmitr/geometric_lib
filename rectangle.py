def area(a: int, b: int) -> int:
    """
    Вычисление площади прямоугольника по длинам его сторон

    Параметры:
        a: int - Длина первой стороны
        b: int - Длина второй стороны

    Возвращаемое значение: int - Площадь прямоугольника
    >>> area(2, 3)
    6
    """
    return a * b


def perimeter(a: int, b: int) -> int:
    """
    Вычисление периметра прямоугольника по длинам его сторон

    Параметры:
        a: int - Длина первой стороны
        b: int - Длина второй стороны

    Возвращаемое значение: int - Периметр прямоугольника
    >>> perimeter(1,3)
    8
    """
    return (a + b) * 2
