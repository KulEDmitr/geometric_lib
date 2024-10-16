def area(a, b):
    '''
    Принимает на вход стороны a и b, возвращает площадь прямоугольника

    Args:
        a, b (int or float): стороны прямоугольника

    Returns:
        int or float: площадь прямоугольника

    Examples:
        >>> area(3, 4)
        12
        >>> area(2.5, 4)
        10
    '''
    return a * b

def perimeter(a, b):
    '''
    Принимает на вход стороны а и b, возвращает периметр прямоугольнка

    Args:
        a, b (int or float): стороны прямоугольника

    Returns:
        int or float: периметр прямоугольника

    Examples:
        >>> perimeter(1, 7)
        16
        >>> perimeter(2.5, 7)
        19
    '''
    return (a + b) * 2
