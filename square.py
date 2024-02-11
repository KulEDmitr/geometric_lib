import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(0)
        self.assertEquals(res, 0)

    def test_zero_perimeter_mul(self):
        res = perimeter(0)
        self.assertEquals(res, 0)

    def test_big_area_mul(self):
        res = area(200000)
        self.assertEquals(res, 40_000_000_000)

    def test_big_perimeter_mul(self):
        res = perimeter(1000000000)
        self.assertEquals(res, 4000000000)

    def test_float_area_mul(self):
        res = area(3.6)
        self.assertEquals(res, 12.96)

    def test_float_perimeter_mul(self):
        res = perimeter(3.123)
        self.assertEquals(res, 12.492)

    def test_str_area_mul(self):
        self.assertRaises(ValueError, area, "10")

    def test_str_perimeter_mul(self):
        self.assertRaises(ValueError, perimeter, "10")


def area(a):
    """ Returns area of the square with given side

    :param a: side of th square
    :type a: float

    :return: area of the square
    :rtype: float

    area(1.1) = 1.21
    """

    return a * a


def perimeter(a):
    """ Returns perimeter of the square with given side

    :param a: side of th square
    :type a: float

    :return: perimeter of the square
    :rtype: float

    perimeter(59.75) = 239.0
    """

    return 4 * a
