import square
import unittest


class SquareTestCase(unittest.TestCase):
    def test_area_zero_int(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-10)

    def test_area_str_input(self):
        with self.assertRaises(TypeError):
            square.area("a")

    def test_area_none_value(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_area_big_value(self):
        res = square.area(10**10)
        self.assertEqual(res, 100000000000000000000)

    def test_area_small_velue(self):
        res = square.area(10 ** - 10)
        self.assertEqual(res, 1.0000000000000001e-20)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-10)

    def test_perimeter_str_input(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")

    def test_perimeter_none_value(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)
