import unittest

def area(a, b):
    '''Принимает на вход числа а и b - стороны прямоугольника, возвращает a*b - площадь прямоугольника'''
    return a*b



def perimeter(a, b):
    '''Принимает на вход числа a и b - стороны прямоугольника, возвращает 2*(a+b) - периметр прямоугольника'''
    return 2*(a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul_0(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_mul_1(self):
        res = area(0,0)
        self.assertEqual(res, 0)

    def test_zero_mul_2(self):
        res = area(1000,1000)
        self.assertEqual(res, 1000000)

    def test_not_zero_mul_0(self):
        res = area(12, 94)
        self.assertEqual(res, 1128)

    def test_not_zero_mul_1(self):
        res = area(12, 5)
        self.assertNotEqual(res, 59)

    def test_perimeter_0(self):
        res = perimeter(1,5)
        self.assertEqual(res, 12)

    def test_perimeter_1(self):
        self.assertNotEqual(5757, perimeter('5', '7'))

    def test_perimeter_2(self):
        self.assertRaises(TypeError, perimeter, 2, '5')

    def test_perimeter_3(self):
        self.assertEqual(perimeter(-2,-2), -8)
