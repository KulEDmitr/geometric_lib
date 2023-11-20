import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_area_0(self):
        result = area(0)
        self.assertEqual(result, 0)
    def test_area_1(self):
        result = area(10)
        self.assertEqual(result, 314.1592653589793)
    def test_area_2(self):
        result = area(12356)
        self.assertEqual(result, 479629262.6357468)
    def test_area_3(self):
        result = area(-19)
        self.assertEqual(result, "radius can't be less than 0!")
    def test_area_4(self):
        result = area(2147483647)
        self.assertEqual(result, 1.4488038902661206e+19)

    def test_perimeter_0(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    def test_perimeter_1(self):
        result = perimeter(10)
        self.assertEqual(result, 62.83185307179586)
    def test_perimeter_2(self):
        result = perimeter(12356)
        self.assertEqual(result, 77635.03765551097)
    def test_perimeter_3(self):
        result = perimeter(-19)
        self.assertEqual(result, "radius can't be less than 0!")
    def test_perimeter_4(self):
        result = perimeter(2147483647)
        self.assertEqual(result, 13493037698.238832)

def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            area (int): площадь круга

        Пример вызова:
            area(10) = 314.1592653589793
    '''
    if r < 0:
        return "radius can't be less than 0!"
    else:
        return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            perimeter (int): периметр круга

        Пример вызова:
            perimeter(10) = 62.83185307179586
    '''
    if r < 0:
        return "radius can't be less than 0!"
    else:
        return 2 * math.pi * r

