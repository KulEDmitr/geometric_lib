import triangle
import unittest


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_int(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_float(self):
        res = triangle.area(10.6, 0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-10, 10)
        with self.assertRaises(ValueError):
            triangle.area(10, -10)

    def test_area_str_input(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 10)
        with self.assertRaises(TypeError):
            triangle.area(10, "a")

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-10, 10, 10)

    def test_area_none_value(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 10)
        with self.assertRaises(TypeError):
            triangle.area(10, None)

    def test_area_big_value(self):
        res = triangle.area(10**10, 10**5)
        self.assertEqual(res, 500000000000000.0)

    def test_area_small_velue(self):
        res = triangle.area(10 ** - 10, 10 ** 5)
        self.assertEqual(res,  5e-06)

    def test_perimeter_zero_int(self):
        res = triangle.perimeter(10, 0, 20)
        self.assertEqual(res, 30)

    def test_perimeter_zero_float(self):
        res = triangle.perimeter(10.5, 0, 10.5)
        self.assertEqual(res, 21)

    def test_perimeter_equilateral_int(self):
        res = triangle.perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_equilateral_float(self):
        res = triangle.perimeter(10.5, 10.5, 10.5)
        self.assertEqual(res, 31.5)

    def test_perimetr_str_input(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("a", 50, 50)
        with self.assertRaises(TypeError):
            triangle.perimeter(50, "a", 50)
        with self.assertRaises(TypeError):
            triangle.perimeter(50, 50, "a")

    def test_perimeter_none_value(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(None, 10, 50)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, None, 50)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, 10, None)
