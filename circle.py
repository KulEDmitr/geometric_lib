import unittest
import math


def area(r):
    """
    print(area(10)) # 314.1592653589793 

    Возвращает площадь круга с указанным радиусом

        Параметры:
            r (int) - радиус круга

        Возвращаемое значение:
            circle_area (int) - площадь круга с радиусом r
    """
    return math.pi * r * r


def perimeter(r):
    """                                                  
    print(perimeter(10)) # 62.83185307179586
    
    Возвращает длину окружности с указанным радиусом

        Параметры:
            r (int) - радиус круга

        Возвращаемое значение:
            circle_perimeter (int) - длина окружности с радиусом r
    """
    return 2 * math.pi * r

class CircleAreaTestCase(unittest.TestCase):
    def test_area_negative_radius(self):
        self.assertRaisesRegex(ValueError, "Incorrect argument", area, -5)

    def test_area_zero_radius(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, 9)

    def test_area(self):
        res = area(10)
        self.assertAlmostEqual(res, math.pi * 100, 9)

    def test_area_string_argument(self):
        self.assertRaisesRegex(ValueError, "Incorrect argument", area, "12")

class CircleCircumferenceTestCase(unittest.TestCase):
    def test_circumference_negative_radius(self):
        self.assertRaisesRegex(ValueError, "Incorrect argument", perimeter, -14)

    def test_circumference_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circumference(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, math.pi, 9)

    def test_circumference_string(self):
        self.assertRaisesRegex(ValueError, "Incorrect argument", perimeter, "7")
