import unittest
import math
from new_version import (circle_area, circle_perimeter, rectangle_area,
                         rectangle_perimeter, square_area, square_perimeter,
                         triangle_area, triangle_perimeter)

class TestShapesFunctions(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.41592653589793)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-5)

    def test_circle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            circle_perimeter("string")

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_rectangle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "string")

    def test_square_area(self):
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square_area(-5)

    def test_square_area_invalid_type(self):
        with self.assertRaises(TypeError):
            square_area("string")

    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 10), 25)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            triangle_area(5, -10)

    def test_triangle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle_perimeter(3, 4, "string")

if __name__ == '__main__':
    unittest.main()