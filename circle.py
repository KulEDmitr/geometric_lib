import math
import unittest

"""Подключаем библиотеку math для работы с числом Pi"""


def area(r):
    """
  Принимает число r, возращает произведение из квадрата r и числа Pi;
   Например: area(10) вернет 314.15...
  """
    return math.pi * r * r


def perimeter(r):
    """
  Принимает число r, возращает произведение из 2*r и числа Pi;
  Например: perimetr(8) вернет 16 * 3,1415..
  """
    return 2 * math.pi * r


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_square_mul(self):
        res = area(9)
        self.assertEqual(res, 81 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_typical_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def string_test(self):
        res = perimeter("10")
        self.assertEqual(res, 20 * math.pi)
