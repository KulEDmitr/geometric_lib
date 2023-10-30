import math


def area(r):
    """ Returns area of the circle with given radius

    :param r: radius of the circle
    :type r: float

    :return: area of the circle
    :rtype: float

    area(1.0) = 3.14159265358
    """

    return math.pi * r * r


def perimeter(r):
    """ Returns perimeter of the circle with given radius

    :param r: radius of the circle
    :type r: float

    :return: perimeter of the circle
    :rtype: float

    perimeter(0.5) = 3.14159265358
    """

    return 2 * math.pi * r

