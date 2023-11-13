import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(2, 0)
        self.assertEquals(res, 0)

    def test_zero_perimeter_mul(self):
        res = perimeter(2, 0, 3)
        self.assertEquals(res, None)

    def test_big_area_mul(self):
        res = area(20000, 100000)
        self.assertEquals(res, 1_000_000_000)

    def test_big_perimeter_mul(self):
        res = perimeter(1000, 1000, 1000)
        self.assertEquals(res, 3000)

    def test_float_area_mul(self):
        res = area(3.6, 13.8)
        self.assertEquals(res, 24.84)

    def test_float_perimeter_mul(self):
        res = perimeter(3.123, 2.123, 4.34)
        self.assertEquals(res, 9.586)

    def test_str_area_mul(self):
        self.assertRaises(ValueError, area, 10, "10")

    def test_str_perimeter_mul(self):
        self.assertRaises(ValueError, perimeter, 10, "10", 10)

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