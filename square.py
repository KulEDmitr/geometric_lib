
def area(a):
    """
    Принимает длину стороны квадрата, возвращает его площадь

    Параметр:
        a (int): длина стороны квадрата
    Возвращаемое значение:
        a * a (int): площадь квадрата

    Примеры:
        area(3) --> 9
        area(2) --> 4
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")

    return a * a


def perimeter(a):
    """
    Принимает длину стороны квадрата, возвращает его периметр

    Параметр:
        a (int): длина стороны квадрата
    Возвращаемое значение:
        4 * a (int): периметр квадрата

    Примеры:
        perimeter(3) --> 12
        perimeter(2) --> 8
    """

    if a <= 0:
        raise ValueError("length can't be negative or equal to zero")

    return 4 * a
