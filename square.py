
def area(a):
    """
    Вычисляет площадь квадрата.

    Параметры:
        a (float): длина стороны квадрата.

    Возвращаемое значение:
        (float): площадь квадрата.

    Пример использования:
        >>> square.area(4)
        16
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом")

    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата.

    Параметры:
        a (float): длина стороны квадрата.

    Возвращаемое значение:
        (float): периметр квадрата.

    Пример использования:
        >>> square.perimeter(8)
        32
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом")

    if a < 0:
        raise ValueError("Сторона не может быть отрицательным")

    return 4 * a
