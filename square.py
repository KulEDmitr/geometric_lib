def area_square(a):
    '''
    Вычисляет площадь квадрата по длине стороны.

    Параметры:
        a (int/float): длина стороны квадрата

    Возвращаемое значение:
        float: площадь квадрата

    Пример вызова:
        area_square(4) -> 16
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a number")
    if a < 0:
        raise ValueError("Side length cannot be negative")
    if a > 1_000_000:
        raise ValueError("Side length is too large")
    return a * a


def perimeter_square(a):
    '''
    Вычисляет периметр квадрата по длине стороны.

    Параметры:
        a (int/float): длина стороны квадрата

    Возвращаемое значение:
        float: периметр квадрата

    Пример вызова:
        perimeter_square(4) -> 16
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a number")
    if a < 0:
        raise ValueError("Side length cannot be negative")
    if a > 1_000_000:
        raise ValueError("Side length is too large")
    return 4 * a
