import circle
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-10)

    def test_area_str_input(self):
        with self.assertRaises(TypeError):
            circle.area("a")

    def test_area_none_value(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_area_big_value(self):
        res = circle.area(10**10)
        self.assertEqual(res, 3.1415926535897933e+20 )

    def test_area_small_velue(self):
        res = circle.area(10 ** - 10)
        self.assertEqual(res, 3.1415926535897936e-20)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-10)

    def test_perimeter_str_input(self):
        with self.assertRaises(TypeError):
            circle.perimeter("a")

    def test_perimeter_none_value(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)