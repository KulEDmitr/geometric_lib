import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(25)
        self.assertEqual(res, 625)

    def test_square_perim_13(self):
        res = perimeter(13)
        self.assertEqual(res, 52)
    
    def test_square_perim_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_square_perim_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


def area(a):
    '''Принимает длину сторон квадрата, возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает длину сторон квадрата, возвращает периметр квадрата'''
    return 4 * a
