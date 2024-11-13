# test_rectangle.py
import unittest
from rectangle import area, perimeter  # импортируем тестируемые функции

class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area(5, 10), 50, "Expected area to be 50 for a rectangle 5x10")

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0, "Expected area to be 0 when one side is 0")

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100, "Expected area to be 100 for a square of side 10")

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40, "Expected perimeter to be 40 for a square of side 10")

    def test_area_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            area(-5, 10)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            perimeter(-5, 10)

    def test_area_large_values(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large dimensions"):
            area(2_000_000, 2_000_000)

    def test_perimeter_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter("a", 5)

if __name__ == "__main__":
    unittest.main()
