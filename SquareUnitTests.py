import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_int_value_one(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_int_value_two(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_float_value(self):
        res = area(5.5)
        self.assertEqual(res, 30.25)

    def test_area_big_value(self):
        res = area(1010101)
        self.assertEqual(res, 1_020_304_030_201)

    def test_area_zero_value(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_int_value_one(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_int_value_two(self):
        res = perimeter(20)
        self.assertEqual(res, 80)

    def test_perimeter_float_value(self):
        res = perimeter(4.1)
        self.assertEqual(res, 16.4)

    def test_perimeter_big_value(self):
        res = perimeter(101010101)
        self.assertEqual(res, 404040404)

    def test_perimeter_zero_value(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
