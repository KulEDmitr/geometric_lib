import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_num(self):
        res = area(10)
        self.assertEqual(res, 314.159265358979)

    def test_area_str_arg(self):
        self.assertRaises(area("10"), Exception)

    def test_area_arr_arg(self):
        self.assertRaises(area([10]), Exception)

    def test_area_neg_arg(self):
        self.assertRaises(area(-10), Exception)

    def test_area_big_num(self):
        res = area(2147483647)
        self.assertEqual(res, 14488038902661200000)

    def test_area_float_num_1(self):
        res = area(10.0)
        self.assertEqual(res, 314.159265358979)

    def test_area_float_num_2(self):
        res = area(0.000000001)
        self.assertEqual(res, 0.00000000000000000314159265358979)

    def test_area_big_float_num(self):
        res = area(0.00000000000000000001)
        self.assertEqual(res, 3.14159265358979*10**(-40))

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_num(self):
        res = perimeter(10)
        self.assertEqual(res, 62.8318530717958)

    def test_perimeter_str_arg(self):
        self.assertRaises(perimeter("10"), Exception)

    def test_perimeter_arr_arg(self):
        self.assertRaises(perimeter([10]), Exception)

    def test_perimeter_neg_arg(self):
        self.assertRaises(perimeter(-10), Exception)

    def test_perimeter_big_num(self):
        res = perimeter(2147483647)
        self.assertEqual(res, 13493037698.238)

    def test_perimeter_float_num(self):
        res = perimeter(10.0)
        self.assertEqual(res, 62.8318530717958)

    def test_perimeter_big_float_num(self):
        res = perimeter(0.00000000000000000001)
        self.assertEqual(res, 0.000000000000000000062831853072)

    def test_perimeter_float_num(self):
        res = perimeter(0.000000001)
        self.assertEqual(res, 0.00000000628318530717958)

