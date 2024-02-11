import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(0)
        self.assertEquals(res, 0)

    def test_zero_perimeter_mul(self):
        res = perimeter(0)
        self.assertEquals(res, 0)

    def test_big_area_mul(self):
        res = area(200000)
        self.assertEquals(res, 125663706143.59172)

    def test_big_perimeter_mul(self):
        res = perimeter(1000000000)
        self.assertEquals(res, 6283185307.179586)

    def test_float_area_mul(self):
        res = area(3.6)
        self.assertEquals(res, 40.71504079052372)

    def test_float_perimeter_mul(self):
        res = perimeter(3.123)
        self.assertEquals(res, 19.62238771432185)

    def test_str_area_mul(self):
        self.assertRaises(ValueError, area, "10")

    def test_str_perimeter_mul(self):
        self.assertRaises(ValueError, perimeter, "10")

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

