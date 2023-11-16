import unittest
import math

"""Подключем библиотеку math для использования pi"""


def area(r):
    """Пример вызова функции:

    def area(3):
        if 3 == 0:
            return None
        else:
            return 9*3,14

    Функция принимает r <- радиус круга. Если R = 0, то круга не существует, иначе функция возвращает его площадь.
    """
    if r == 0:
        return None
    else:
        return math.pi * r * r


def perimeter(r):
    """Пример вызова функции:

    def perimeter(3):
        if 3 == 0:
            return None
        else:
            return 6*3,14

    Функция принимает r <- радиус круга. Если R = 0, то круга не существует, иначе функция возвращает длину его окружности.
    """
    if r == 0:
        return None
    else:
        return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertAlmostEqual(area(0), None)
        self.assertAlmostEqual(perimeter(0), None)

    def test_value_mul(self):
        self.assertAlmostEqual(area(3), 28.27, delta=0.01)
        self.assertAlmostEqual(perimeter(3), 18.84, delta=0.01)

    def test_string_radius_perimeter(self):
        with self.assertRaises(TypeError):
            res = perimeter("A")

    def test_string_radius_area(self):
        with self.assertRaises(TypeError):
            res = area("A")
