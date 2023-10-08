import math


def area(r):
    """ Returns area of the circle with given radius

    :param r: radius of the circle
    :type r: float

    :return: area of the circle
    :rtype: float
    """

    return math.pi * r * r


def perimeter(r):
    """ Returns perimeter of the circle with given radius

    :param r: radius of the circle
    :type r: float

    :return: perimeter of the circle
    :rtype: float
    """

    return 2 * math.pi * r

