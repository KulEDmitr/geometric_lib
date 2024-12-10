import rectangle
import unittest


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-10, 0)

    def test_area_str_input(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 10)

    def test_area_none_value(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 10)
        with self.assertRaises(TypeError):
            rectangle.area(10, None)

    def test_area_big_value(self):
        res = rectangle.area(10**10, 10**5)
        self.assertEqual(res, 0)

    def test_area_small_velue(self):
        res = rectangle.area(10 ** - 10, 10 ** 5)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_square(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-10, 0)

    def test_perimeter_str_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("a", 0)

    def test_perimeter_none_value(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 10)
        with self.assertRaises(TypeError):
            rectangle.perimeter(10, None)