import unittest
from triangle import area_triangle, perimeter_triangle  # импортируем тестируемые функции


class TriangleTestCase(unittest.TestCase):

    def test_area_triangle(self):
        self.assertEqual(area_triangle(5, 3), 7.5, "Expected area_triangle to be 7.5 for base 5 and height 3")

    def test_area_triangle_zero_base(self):
        self.assertEqual(area_triangle(0, 3), 0, "Expected area_triangle to be 0 for base 0")

    def test_area_triangle_zero_height(self):
        self.assertEqual(area_triangle(5, 0), 0, "Expected area_triangle to be 0 for height 0")

    def test_area_triangle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            area_triangle(-5, 3)

    def test_area_triangle_large_values(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large dimensions"):
            area_triangle(2_000_000, 2_000_000)

    def test_area_triangle_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            area_triangle("a", 5)

    def test_perimeter_triangle(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12, "Expected perimeter_triangle to be 12 for sides 3, 4, 5")

    def test_perimeter_triangle_zero(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0, "Expected perimeter_triangle to be 0 for all sides 0")

    def test_perimeter_triangle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative side lengths"):
            perimeter_triangle(-3, 4, 5)

    def test_perimeter_triangle_large_values(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large side lengths"):
            perimeter_triangle(2_000_000, 2_000_000, 2_000_000)

    def test_perimeter_triangle_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter_triangle("a", 4, 5)


if __name__ == "__main__":
    unittest.main()
