# test_rectangle.py
import unittest
from rectangle import area_rectangle, perimeter_rectangle  # импортируем тестируемые функции

class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle_valid(self):
        """Тест площади прямоугольника с валидными положительными значениями."""
        self.assertEqual(area_rectangle(5, 10), 50, "Expected area_rectangle to be 50 for a rectangle 5x10")

    def test_area_rectangle_zero_side(self):
        """Тест площади прямоугольника, если одна из сторон равна нулю."""
        self.assertEqual(area_rectangle(10, 0), 0, "Expected area_rectangle to be 0 when one side is 0")

    def test_area_rectangle_both_zero(self):
        """Тест площади прямоугольника, если обе стороны равны нулю."""
        self.assertEqual(area_rectangle(0, 0), 0, "Expected area_rectangle to be 0 when both sides are 0")

    def test_area_rectangle_square(self):
        """Тест площади квадрата."""
        self.assertEqual(area_rectangle(10, 10), 100, "Expected area_rectangle to be 100 for a square of side 10")

    def test_perimeter_rectangle_square(self):
        """Тест периметра квадрата."""
        self.assertEqual(perimeter_rectangle(10, 10), 40, "Expected perimeter_rectangle to be 40 for a square of side 10")

    def test_area_rectangle_negative(self):
        """Тест на выброс ValueError при отрицательных значениях сторон."""
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            area_rectangle(-5, 10)

    def test_perimeter_rectangle_negative(self):
        """Тест на выброс ValueError при отрицательных значениях сторон."""
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions"):
            perimeter_rectangle(-5, 10)

    def test_area_rectangle_large_values(self):
        """Тест на выброс ValueError при слишком больших значениях сторон."""
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large dimensions"):
            area_rectangle(2_000_000, 2_000_000)

    def test_perimeter_rectangle_non_numeric(self):
        """Тест на выброс TypeError при нечисловых значениях."""
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter_rectangle("a", 5)

    def test_area_rectangle_non_numeric(self):
        """Тест на выброс TypeError при нечисловых значениях для площади."""
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            area_rectangle("b", 10)

    def test_perimeter_rectangle_large_values(self):
        """Тест на выброс ValueError при слишком больших значениях для периметра."""
        with self.assertRaises(ValueError, msg="Expected ValueError for excessively large dimensions"):
            perimeter_rectangle(1_000_000, 1_000_000)

if __name__ == "__main__":
    unittest.main()
