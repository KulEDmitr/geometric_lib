import unittest
from circle import area_circle, perimeter_circle  # импортируем тестируемые функции


class CircleTestCase(unittest.TestCase):

    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(5), 78.53981633974483, msg="Expected area_circle to be ~78.54 for radius 5")

    def test_area_circle_zero(self):
        self.assertEqual(area_circle(0), 0, "Expected area_circle to be 0 for radius 0")

    def test_area_circle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative radius"):
            area_circle(-5)

    # def test_area_circle_large_values(self):
    #     with self.assertRaises(ValueError, msg="Expected ValueError for excessively large radius"):
    #         area_circle(2_000_000)

    def test_area_circle_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            area_circle("r")

    def test_perimeter_circle(self):
        self.assertAlmostEqual(perimeter_circle(5), 31.41592653589793, msg="Expected perimeter_circle to be ~31.42 for radius 5")

    def test_perimeter_circle_negative(self):
        with self.assertRaises(ValueError, msg="Expected ValueError for negative radius"):
            perimeter_circle(-5)

    # def test_perimeter_circle_large_values(self):
    #     with self.assertRaises(ValueError, msg="Expected ValueError for excessively large radius"):
    #         perimeter_circle(2_000_000)

    def test_perimeter_circle_non_numeric(self):
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric input"):
            perimeter_circle(None)


if __name__ == "__main__":
    unittest.main()
