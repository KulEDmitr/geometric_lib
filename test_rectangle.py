# test_rectangle.py
import unittest
from rectangle import area_rectangle, perimeter_rectangle  # импортируем тестируемые функции

class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle_rectangle(self):
        self.assertEqual(area_rectangle(5, 10), 50, "Expected area_rectangle to be 50 for a rectangle 5x10")

    def test_area_rectangle_zero(self):
        self.assertEqual(area_rectangle(10, 0), 0, "Expected area_rectangle to be 0 when one side is 0")

    def test_area_rectangle_square(self):
        self.assertEqual(area_rectangle(10, 10), 100, "Expected area_rectangle to be 100 for a square of side 10")

    def test_perimeter_rectangle_square(self):
        self.assertEqual(perimeter_rectangle(10, 10), 40, "Expected perimeter_rectangle to be 40 for a square of side 10")

    def test_area_rectangle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            area_rectangle(-5, 10)

    def test_perimeter_rectangle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            perimeter_rectangle(-5, 10)

    def test_area_rectangle_large_values(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large dimensions"):
            area_rectangle(2_000_000, 2_000_000)

    def test_perimeter_rectangle_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter_rectangle("a", 5)

if __name__ == "__main__":
    unittest.main()
