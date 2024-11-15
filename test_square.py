import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_with_zero_side(self):
        # Проверка площади квадрата со стороной 0
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_with_positive_side(self):
        # Проверка площади квадрата с положительной стороной
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_with_negative_side(self):
        # Проверка площади квадрата с отрицательной стороной
        res = area(-5)
        self.assertEqual(res, 25)

    def test_perimeter_with_zero_side(self):
        # Проверка периметра квадрата со стороной 0
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_with_positive_side(self):
        # Проверка периметра квадрата с положительной стороной
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_with_negative_side(self):
        # Проверка периметра квадрата с отрицательной стороной
        res = perimeter(-5)
        self.assertEqual(res, -20)
