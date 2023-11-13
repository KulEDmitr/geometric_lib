import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(2, 0)
        self.assertEquals(res, 0)

    def test_zero_perimeter_mul(self):
        res = perimeter(2, 0)
        self.assertEquals(res, 4)

    def test_big_area_mul(self):
        res = area(20000, 100000)
        self.assertEquals(res, 2_000_000_000)

    def test_big_perimeter_mul(self):
        res = perimeter(1000, 5000)
        self.assertEquals(res, 12000)

    def test_float_area_mul(self):
        res = area(3.6, 13.8)
        self.assertEquals(res, 49.68)

    def test_float_perimeter_mul(self):
        res = perimeter(3.123, 2.123)
        self.assertEquals(res, 10.492)

    def test_str_area_mul(self):
        self.assertRaises(ValueError, area, 10, "10")

    def test_str_perimeter_mul(self):
        self.assertRaises(ValueError, perimeter, 10, "10")


def area(a, b):
    """ Returns area of the rectangle with given sides

    :param a: first side
    :type a: float

    :param b: second side
    :type b: float

    :return: area of the rectangle
    :rtype: float

    area(1.0, 3.5) = 3.5
    """

    return a * b


def perimeter(a, b):
    """ Returns perimeter of the rectangle with given sides

    :param a: first side
    :type a: float

    :param b: second side
    :type b: float

    :return: perimeter of the rectangle
    :rtype: float

    perimeter(32, 1) = 66
    """

    return (a + b) * 2
