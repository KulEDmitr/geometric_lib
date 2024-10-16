def area(a)
    '''
    Площадь квадрата

    Args:
        a (int or float): сторона квадрата

    Returns:
        int or float: площадь квадрата

    Examples:
        >>> area(4)
        16
        >>> area(3.5)
        12.25
    '''
    return a * a


def perimeter(a):
    '''
    Периметр квадрата

    Args:
        a (int): сторона квадрата

    Returns:
        int or float: периметр квадрата

    Examples:
        >>> perimeter(5)
        20
        >>> perimeter(3.5)
        14
    '''
    return 4 * a
