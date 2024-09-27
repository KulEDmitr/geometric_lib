import unittest


def area(a, h):
    """
    Функция принимает два катета треугольника, возвращает его площад;
    Например: area(5, 8) вернет 20
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Функция принимает три стороны треугольника, возвращает его периметр;
   Например: perimetr(5, 8, 4) вернет 17
   """

    return a + b + c


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(20, 8)
        self.assertEqual(res, 80)

    def test_big_mul(self):
        res = area(1000000000000, 1000000000)
        self.assertEqual(res, 500000000000000000000)

    def test_zero_perimeter(self):
        res = perimeter(5, 0, 22)
        self.assertEqual(res, 27)

    def test_typical_perimeter(self):
        res = perimeter(11, 22, 33)
        self.assertEqual(res, 66)
