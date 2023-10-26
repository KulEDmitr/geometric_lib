import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_int_value_one(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_area_int_value_two(self):
        res = area(7, 3)
        self.assertEqual(res, 10.5)

    def test_area_float_value(self):
        res = area(5.5, 1.4)
        self.assertEqual(res, 3.85)

    def test_area_big_value(self):
        res = area(10_000, 10_000)
        self.assertEqual(res, 50_000_000)

    def test_area_zero_value(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_perimeter_int_value_one(self):
        res = perimeter(10, 5, 3)
        self.assertEqual(res, 18)

    def test_perimeter_int_value_two(self):
        res = perimeter(7, 3, 10)
        self.assertEqual(res, 20)

    def test_perimeter_float_value(self):
        res = perimeter(5.5, 1.3, 1.1)
        self.assertEqual(res, 7.9)

    def test_perimeter_big_value(self):
        res = perimeter(10_000, 10_000, 10_000)
        self.assertEqual(res, 30_000)

    def test_perimeter_zero_value(self):
        res = perimeter(5, 0, 0)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
