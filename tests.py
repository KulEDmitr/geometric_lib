import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestGeometricFunctions(unittest.TestCase):

    # Тесты для модуля circle.py
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), math.pi * 3 ** 2)
        self.assertAlmostEqual(circle_area(0.45), math.pi * 0.45 ** 2)

    def test_circle_perimeter_valid(self):
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3)
        self.assertAlmostEqual(circle_perimeter(0.45), 2 * math.pi * 0.45)

    def test_circle_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            circle_perimeter(0)

    # Тесты для модуля rectangle.py
    def test_rectangle_area_valid(self):
        self.assertEqual(rectangle_area(3, 4), 3 * 4)
        self.assertEqual(rectangle_area(1, 0.45), 1 * 0.45)

    def test_rectangle_perimeter_valid(self):
        self.assertEqual(rectangle_perimeter(3, 4), 2 * (3 + 4))
        self.assertEqual(rectangle_perimeter(1, 0.45), 2 * (1 + 0.45))

    def test_rectangle_invalid(self):
        with self.assertRaises(ValueError):
            rectangle_area(-1, 4)
        with self.assertRaises(ValueError):
            rectangle_perimeter(3, -1)

    # Тесты для модуля triangle.py
    def test_triangle_area_valid(self):
        self.assertAlmostEqual(triangle_area(3, 3), 3 * 3 / 2)
        self.assertAlmostEqual(triangle_area(0.45, 2), 0.45 * 2 / 2)

    def test_triangle_perimeter_valid(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 3 + 4 + 5)
        self.assertEqual(triangle_perimeter(1, 2, 2), 1 + 2 + 2)

    def test_triangle_invalid(self):
        with self.assertRaises(ValueError):
            triangle_area(-1, 2)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, -4, 5)

    # Тесты для модуля square.py
    def test_square_area_valid(self):
        self.assertEqual(square_area(3), 3 ** 2)
        self.assertEqual(square_area(0.45), 0.45 ** 2)

    def test_square_perimeter_valid(self):
        self.assertEqual(square_perimeter(3), 4 * 3)
        self.assertEqual(square_perimeter(0.45), 4 * 0.45)

    def test_square_invalid(self):
        with self.assertRaises(ValueError):
            square_area(-1)
        with self.assertRaises(ValueError):
            square_perimeter(0)


if __name__ == "__main__":
    unittest.main()
