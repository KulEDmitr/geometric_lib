import circle
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_positive_int_values(self):
        res = circle.area(5)
        self.assertAlmostEqual(78.53981633974483, res, places=6)

    def test_area_positive_float_values(self):
        res = circle.area(5.0)
        self.assertAlmostEqual(78.53981633974483, res, places=6)

    def test_area_zero_values(self):
        res = circle.area(0)
        self.assertEqual(0, res)

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            circle.area(-5.0)

    def test_area_string_value(self):
        with self.assertRaises(TypeError):
            circle.area("5.0")

    def test_perimeter_positive_int_values(self):
        res = circle.perimeter(7)
        self.assertAlmostEqual(43.982297150257104, res, places=6)

    def test_perimeter_positive_float_values(self):
        res = circle.perimeter(7.0)
        self.assertAlmostEqual(43.982297150257104, res, places=6)

    def test_perimeter_zero_values(self):
        res = circle.perimeter(0)
        self.assertEqual(0, res)

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-7.0)

    def test_perimeter_string_value(self):
        with self.assertRaises(TypeError):
            circle.perimeter("7.0")
