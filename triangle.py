import unittest


def area(a, h):
    '''принимает длину основания и высоты - возвращает площадь
    a = 3; h = 6
    area = 9
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''принимает длины трех сторон - возвращает периметр
    a = 5; b = 6; c = 10
    perimeter = 21
    '''
    return a + b + c


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_negative_value(self):
        res = area(-10, -10)
        self.assertEqual(res, 50)
