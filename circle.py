import math
import unittest


def area(r):
    """
    Принимает радиус круга и возвращает его площадь.

    Пример:
        Ввод:
        5

        Вывод:
        78.53981633974483
    :param r: Радиус круга.
    :return: Площадь.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Принимает радиус круга и возвращает его периметр.

    Пример:
        Ввод:
        5

        Вывод:
        31.41592653589793
    :param r: Радиус круга.
    :return: Периметр.
    """
    return 2 * math.pi * r


class CircleTests(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 78.53981633974483)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(-5), 78.53981633974483)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(-5), -31.41592653589793)
