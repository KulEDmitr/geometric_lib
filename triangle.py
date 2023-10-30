def area(a, h):
    """ Returns area of the triangle with given side and height drawn to this side

    :param a: side
    :type a: float

    :param h: height
    :type h: float

    :return: area of the triangle
    :rtype: float

    area(1.0, 4) = 2.0
    """

    return a * h / 2 

def perimeter(a, b, c):
    """Returns area of the triangle with three given sides

    :param a: first side
    :type a: float

    :param b: second side
    :type b: float

    :param c: third side
    :type c: float

    :return: perimeter of the triangle
    :rtype: float

    perimeter(11.9, 12.1, 10.2) = 34.2
    """

    return a + b + c 