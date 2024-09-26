import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_num(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_str_arg(self):
        self.assertRaises(area("10"), Exception)

    def test_area_arr_arg(self):
        self.assertRaises(area([10]), Exception)

    def test_area_neg_arg(self):
        self.assertRaises(area(-10), Exception)

    def test_area_big_num(self):
        res = area(2147483647)
        self.assertEqual(res, 4611686014132420609)

    def test_area_float_num_1(self):
        res = area(10.0)
        self.assertEqual(res, 100.0)

    def test_area_float_num_2(self):
        res = area(0.000000001)
        self.assertEqual(res, 0.000000000000000001)

    def test_area_big_float_num(self):
        res = area(0.00000000000000000001)
        self.assertEqual(res, 0.0000000000000000000000000000000000000001)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_num(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_str_arg(self):
        self.assertRaises(perimeter("10"), Exception)

    def test_perimeter_arr_arg(self):
        self.assertRaises(perimeter([10]), Exception)

    def test_perimeter_neg_arg(self):
        self.assertRaises(perimeter(-10), Exception)

    def test_perimeter_big_num(self):
        res = perimeter(2147483647)
        self.assertEqual(res, 8589934588)

    def test_perimeter_float_num(self):
        res = perimeter(10.0)
        self.assertEqual(res, 40.0)

    def test_perimeter_big_float_num(self):
        res = perimeter(0.00000000000000000001)
        self.assertEqual(res, 0.00000000000000000004)

    def test_perimeter_float_num(self):
        res = perimeter(0.000000001)
        self.assertEqual(res, 0.000000004)
