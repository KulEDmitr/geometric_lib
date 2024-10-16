def area(a, h):
    '''
    Принимает на вход сторону а и высоту h, возвращает площадь треугольника

    Args:
        a, h (int or float): стороны и высота треугольника

    Returns:
        int or float: площадь треугольника

    Examples:
        >>> area(6, 7)
        21
        >>> area(2, 3)
        3
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает на вход 3 стороны треугольника

    Args:
        a, b, c (int or float): стороны треугольника

    Returns:
        int or float: площадь треугольника

    Examples:
        >>> perimeter(3, 4, 5)
        12
        >>> perimeter(1.5, 2, 5)
        8.5
    '''
    return a + b + c
