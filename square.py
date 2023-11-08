import unittest

def area(a):
    '''Принимает на вход a - сторону квадрата, возвращает a*a - площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает на вход a - сторону квадрата, возвращает 4*a - периметр квадрата'''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_2(self):
        self.assertRaises(TypeError, area, '5')

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_2(self):
        res = perimeter(-2)
        self.assertEqual(res, -8)

    def test_perimeter_3(self):
        self.assertEqual('5555', perimeter('5'))

