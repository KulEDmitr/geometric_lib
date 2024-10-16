import math


def area(r):
    '''
    Принимает на вход радиус и возвращает площадь круга

    Args:
        r (int or float): радиус круга

    Returns:
        int or float: площадь круга

    Examples:
        >>> area(7)
        153.93804002589985
        >>> area(2.5)
        19.634954084936208
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает на вход радиус и возвращает периметр круга

    Args:
        r (int or float): радиус круга

    Returns:
        int or float: площадь круга

    Examples:
        >>> perimeter(6)
        37.69911184307752
        >>> perimeter(3.6)
        22.61946710584651
    '''
    return 2 * math.pi * r
