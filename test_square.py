import unittest
from square import area_square, perimeter_square  # импортируем тестируемые функции


class SquareTestCase(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(area_square(4), 16, "Expected area_square to be 16 for side length 4")

    def test_area_square_zero(self):
        self.assertEqual(area_square(0), 0, "Expected area_square to be 0 for side length 0")

    def test_area_square_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative side length"):
            area_square(-4)

    # def test_area_square_large_values(self):
    #     with self.assertRaises(ValueError, msg="Expected ValueError for excessively large side length"):
    #         area_square(2_000_000)

    def test_area_square_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            area_square("a")

    def test_perimeter_square(self):
        self.assertEqual(perimeter_square(4), 16, "Expected perimeter_square to be 16 for side length 4")

    def test_perimeter_square_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative side length"):
            perimeter_square(-4)

    # def test_perimeter_square_large_values(self):
    #     with self.assertRaises(ValueError, msg="Expected ValueError for excessively large side length"):
    #         perimeter_square(2_000_000)

    def test_perimeter_square_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter_square(None)


if __name__ == "__main__":
    unittest.main()
