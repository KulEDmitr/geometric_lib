import unittest
from circle import area, perimeter  
import math

class CircleTestCase(unittest.TestCase):
    def test_area_with_zero_radius(self):
        # Проверка площади окружности с радиусом 0
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_with_positive_radius(self):
        # Проверка площади окружности с положительным радиусом
        res = area(10)
        self.assertAlmostEqual(res, 100 * math.pi, places=5)

    def test_area_with_negative_radius(self):
        # Проверка площади окружности с отрицательным радиусом
        res = area(-10)
        self.assertAlmostEqual(res, 100 * math.pi, places=5)

    def test_perimeter_with_zero_radius(self):
        # Проверка периметра окружности с радиусом 0
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_with_positive_radius(self):
        # Проверка периметра окружности с положительным радиусом
        res = perimeter(10)
        self.assertAlmostEqual(res, 20 * math.pi, places=5)

    def test_perimeter_with_negative_radius(self):
        # Проверка периметра окружности с отрицательным радиусом
        res = perimeter(-10)
        self.assertAlmostEqual(res, -20 * math.pi, places=5)