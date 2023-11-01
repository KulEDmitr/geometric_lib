import math
import unittest

def area(r: float) -> float:
    """
    Возвращает площадь круга радиусом r

	Параметры:
	    r (float): радиус круга

	Возвращаемое значение:
	    circle_area (float): Площадь круга заданного радиуса
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Возвращает периметр круга радиусом r

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        circle_perimeter (float): Периметр круга заданного радиуса
    """

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(0, res)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(0, res)

    def test_area(self):
        res = area(3)
        self.assertEqual(res, 9 * math.pi)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 10 * math.pi)