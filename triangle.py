import unittest


def area(a, h):
    """ 
    Принимает a (сторона треугольника) и h (высота треугольника), и возвращает площадь треугольника.
    Пример работы: area(3, 5) - возвращает 7.5. 
    """
    return a * h / 2


def perimeter(a, b, c):
    """ 
    Принимает a, b и c (стороны треугольника), и возвращает периметр треугольника.
    Пример работы: perimeter(3, 4, 5) - возвращает 12. 
    """
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_simple_numbers(self):
        res = area(8, 4)
        self.assertEqual(res, 16)

    def test_area_zero(self):
        res = area(0, 9)
        self.assertEqual(res, 0)

    def test_area_large_numbers(self):
        res = area(12345000, 12345999)
        self.assertEqual(res, 76205678827500)

    def test_area_negative_numbers(self):
        res = area(-12345000, -12345999)
        self.assertEqual(res, 76205678827500)

    def test_perimeter_simple_numbers(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_large_numbers(self):
        res = perimeter(12345000, 12345999, 12345888)
        self.assertEqual(res, 37036887)

    def test_perimeter_negative_numbers(self):
        res = perimeter(-12345000, -12345999, 12345888)
        self.assertEqual(res, -12345111)
