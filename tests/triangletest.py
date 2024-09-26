import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_positive_int_values(self):
        res = triangle.area(3, 3)
        self.assertAlmostEqual(4.5, res, places=6)

    def test_area_positive_float_values(self):
        res = triangle.area(3.5, 2.5)
        self.assertAlmostEqual(4.375, res, places=6)

    def test_area_zero_values(self):
        res = triangle.area(0, 7)
        self.assertEqual(0, res)

    def test_area_negative_float_values(self):
        with self.assertRaises(ValueError):
            triangle.area(-4.8, 7.1)

    def test_area_string_and_string_values(self):
        with self.assertRaises(TypeError):
            triangle.area("4", "7")

    def test_area_string_and_int_values(self):
        with self.assertRaises(TypeError):
            triangle.area("4", 7)

    def test_area_string_and_float_values(self):
        with self.assertRaises(TypeError):
            triangle.area("4", 7.3)

    def test_perimeter_positive_int_values(self):
        res = triangle.perimeter(3, 2, 4)
        self.assertEqual(9, res)

    def test_perimeter_positive_float_values(self):
        res = triangle.perimeter(3.5, 2.5, 4.0)
        self.assertAlmostEqual(10.0, res, places=6)

    def test_perimeter_zero_values(self):
        res = triangle.perimeter(0, 5, 0)
        self.assertEqual(res, 5)

    def test_perimeter_negative_float_values(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3.5, 2.5, -1.0)

    def test_perimeter_string_and_string_values(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", "5", "4")

    def test_perimeter_string_and_int_values(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", 5, "4")

    def test_perimeter_string_and_float_values(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", 5.3, "4.2")
