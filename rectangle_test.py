import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_a(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_str_arg_a(self):
        self.assertRaises(area("10", 10), Exception)

    def test_area_str_arg_b(self):
        self.assertRaises(area(10, "10"), Exception)

    def test_area_str_arg(self):
        self.assertRaises(area("10", "10"), Exception)

    def test_area_arr_arg_a(self):
        self.assertRaises(area([10], 10), Exception)

    def test_area_arr_arg_b(self):
        self.assertRaises(area(10, [10]), Exception)

    def test_area_arr_arg(self):
        self.assertRaises(area([10], [10]), Exception)

    def test_area_neg_arg_a(self):
        self.assertRaises(area(-10, 10), Exception)

    def test_area_neg_arg_b(self):
        self.assertRaises(area(10, -10), Exception)

    def test_area_neg_arg(self):
        self.assertRaises(area(-10, -10), Exception)

    def test_area_big_num_a(self):
        res = area(2147483647, 100)
        self.assertEqual(res, 214748364700)

    def test_area_big_num_b(self):
        res = area(100, 2147483647)
        self.assertEqual(res, 214748364700)

    def test_area_float_num(self):
        res = area(10.0, 12.0)
        self.assertEqual(res, 120.0)

    def test_area_big_float_num_a(self):
        res = area(0.00000000000000000001, 0.1)
        self.assertEqual(res, 0.000000000000000000001)

    def test_area_big_float_num_b(self):
        res = area(0.1, 0.00000000000000000001)
        self.assertEqual(res, 0.000000000000000000001)

    def test_area_float_num_a(self):
        res = area(0.000000001, 10)
        self.assertEqual(res, 0.00000001)

    def test_area_float_num_b(self):
        res = area(10, 0.000000001)
        self.assertEqual(res, 0.00000001)

    def test_perimeter_zero_a(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 10)

    def test_perimeter_zero_b(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 10)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_str_arg_a(self):
        self.assertRaises(area("10", 10), Exception)

    def test_perimeter_str_arg_b(self):
        self.assertRaises(area(10, "10"), Exception)

    def test_perimeter_str_arg(self):
        self.assertRaises(area("10", "10"), Exception)

    def test_perimeter_arr_arg_a(self):
        self.assertRaises(area([10], 10), Exception)

    def test_perimeter_arr_arg_b(self):
        self.assertRaises(area(10, [10]), Exception)

    def test_perimeter_arr_arg(self):
        self.assertRaises(area([10], [10]), Exception)

    def test_perimeter_neg_arg_a(self):
        self.assertRaises(area(-10, 10), Exception)

    def test_perimeter_neg_arg_b(self):
        self.assertRaises(area(10, -10), Exception)

    def test_perimeter_neg_arg(self):
        self.assertRaises(area(-10, -10), Exception)

    def test_perimeter_big_num(self):
        res = perimeter(2147483647, 2147483647)
        self.assertEqual(res, 8589934588)

    def test_perimeter_float_num(self):
        res = perimeter(10.0, 12.0)
        self.assertEqual(res, 44.0)

    def test_perimeter_big_float_num_a(self):
        res = perimeter(0.00000000000000000001, 0.1)
        self.assertEqual(res, 0.20000000000000000002)

    def test_perimeter_big_float_num_b(self):
        res = perimeter(0.1, 0.00000000000000000001)
        self.assertEqual(res, 0.20000000000000000002)

    def test_perimeter_float_num_a(self):
        res = perimeter(0.000000001, 10)
        self.assertEqual(res, 20.000000002)

    def test_perimeter_float_num_b(self):
        res = perimeter(10, 0.000000001)
        self.assertEqual(res, 20.000000002)
