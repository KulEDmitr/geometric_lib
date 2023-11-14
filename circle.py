import math
import unittest


def area(r):
    """ 
    Принимает r (радиус окружности), и возвращает площадь круга.
    Пример работы: area(1) - возвращает 3.544... 
    """
    return math.pi * r * r


def perimeter(r):
    """ 
    Принимает r (радиус окружности), и возвращает периметр круга.
    Пример работы: perimeter(1) - возвращает 6.283...
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_simple_number(self):
        res = area(10)
        self.assertEqual(round(res), 314)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_large_number(self):
        res = area(12345000)
        self.assertEqual(round(res), 478775657354247)

    def test_area_negative_number(self):
        res = area(-12345000)
        self.assertEqual(round(res), 478775657354247)

    def test_perimeter_simple_number(self):
        res = perimeter(10)
        self.assertEqual(round(res), 63)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_large_number(self):
        res = perimeter(12345000)
        self.assertEqual(round(res), 77565923)

    def test_perimeter_negative_number(self):
        res = perimeter(-12345000)
        self.assertEqual(round(res), -77565923)
