def area(a, b):
    """
    Принимает длину и ширину, возвращает площадь прямоугольника

    Параметры:
        a (int): длина
        h (int): ширина
    Возвращаемое значачение:
        a * h (int): площадь прямоугольника

    Примеры:
        area(3, 5) --> 15
        area(1, 2) --> 2
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")
    elif b <= 0:
        raise ValueError("width can't be negative or equal to zero")

    return a * b


def perimeter(a, b):
    """
    Принимает длину и ширину, возвращает периметр прямоугольника

    Параметры:
        a (int): длина
        h (int): ширина
    Возвращаемое значачение:
        (a + h)*2 (int): периметр прямоугольника

    Примеры:
        perimeter(3, 5) --> 16
        perimeter(1, 2) --> 6
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")
    elif b <= 0:
        raise ValueError("width can't be negative or equal to zero")

    return (a + b)*2
