import unittest


def area(a, b):
    """
    Функция принимает две стороны прямоугольника, возвращает его площадь;
    Например: area(5, 8) вернет 40
    """
    return a * b


def perimeter(a, b):
    """
    Функция принимает две стороны прямоугольника, возвращает его периметр
    Например: perimetr(5, 8) вернет 36
    """
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(52, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_1_perimeter(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 10)

    def test_typical_perimeter(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)
