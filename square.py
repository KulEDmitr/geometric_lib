import unittest


def area(a):
    '''принимает длину стороны квадрата - возвращает площадь
    a = 3
    area = 9
    '''
    return a * a


def perimeter(a):
    '''принимает длину стороны квадрата - возвращает периметр
    a = 5
    perimeter = 20
    '''
    return 4 * a


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_negative_value(self):
        res = area(-10)
        self.assertEqual(res, 100)
