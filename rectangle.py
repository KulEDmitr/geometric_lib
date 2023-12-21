import unittest


def area(a, b):
    '''принимает длины двух сторон прямоугольника - возвращает площадь
    a = 3; b = 4
    area = 12
    '''
    return a * b


def perimeter(a, b):
    '''принимает длины двух сторон прямоугольника - возвращает периметр
    a = 3; b = 5
    perimeter = 16
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_negative_value(self):
        res = area(-10, 10)
        self.assertEqual(res, -100)
