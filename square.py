import unittest

class SquareTestCase(unittest.TestCase):
    def test_square_zero_mul(self):
        res = area(0)
        self.assertEqual(res, "IllegalArgumentException")
    def test_square_int_mul(self):
        res = area(1)
        self.assertEqual(res, 1)
    def test_square_float_mul(self):
        res = area(2.39)
        self.assertEqual(res, 5.7121)
    def test_square_negative_mul(self):
        res = area(-3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_square_string_mul(self):
        res = area('3')
        self.assertEqual(res, "IllegalArgumentException")
    def test_square_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, "IllegalArgumentException")
    def test_square_int_perimeter(self):
        res = perimeter(9)
        self.assertEqual(res, 36)
    def test_square_float_perimeter(self):
        res = perimeter(2.39)
        self.assertEqual(res, 9.56)
    def test_square_negative_perimeter(self):
        res = perimeter(-3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_square_string_perimeter(self):
        res = perimeter('3.1')
        self.assertEqual(res, "IllegalArgumentException")

def area(a):
    '''
    Возвращает площадь квадрата с заданной стороной.

            Параметры:
                    a (float): сторона квадрата

            Возвращаемое значение:
                    square_area (float): площадь квадрата со стороной a

    Примеры вызова функции:
        area(1.0) = 1.0
        area(2.39) = 5.7121
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата с заданной стороной.

            Параметры:
                    a (float): сторона квадрата

            Возвращаемое значение:
                    square_perimeter (float): периметр квадрата со стороной a

    Примеры вызова функции:
        perimeter(1.0) = 4.0
        perimeter(2.39) = 9.56
    '''
    return 4 * a
