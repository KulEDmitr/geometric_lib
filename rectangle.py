import unittest


def area(a, b):
    """ 
    Принимает a и b (стороны прямоугольника), и возвращает площадь прямоугольника.
    Пример работы: area(3, 5) - возвращает 15. 
    """
    return a * b


def perimeter(a, b):
    """ 
    Принимает a и b (стороны прямоугольника), и возвращает периметр прямоугольника.
    Пример работы: perimeter(3, 5) - возвращает 16. 
    """
    return a + b + a + b


class RectangleTestCase(unittest.TestCase):
    def test_area_simple_numbers(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(15, 15)
        self.assertEqual(res, 225)

    def test_area_large_numbers(self):
        res = area(12345000, 12345999)
        self.assertEqual(res, 152411357655000)

    def test_area_negative_numbers(self):
        res = area(-12345000, -12345999)
        self.assertEqual(round(res), 152399025000000)

    def test_perimeter_simple_numbers(self):
        res = perimeter(7, 2)
        self.assertEqual(res, 18)

    def test_perimeter_zero(self):
        res = perimeter(20, 0)
        self.assertEqual(res, 40)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_large_numbers(self):
        res = perimeter(12345000, 12345999)
        self.assertEqual(res, 49381998)

    def test_perimeter_negative_numbers(self):
        res = perimeter(-12345000, -12345999)
        self.assertEqual(round(res), -49381998)
