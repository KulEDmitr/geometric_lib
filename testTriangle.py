import unittest
from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, False)

    def test_zero_2_mul(self):
        res = area(0, 10)
        self.assertEqual(res, False)

    def test_one_mul(self):
        res = area(10, 1)
        self.assertEqual(res, 5)

    def test_odd_mul(self):
        res = area(5, 5)
        self.assertEqual(res, 12.5)

    def test_negative_one_mul(self):
        res = area(10, -1)
        self.assertEqual(res, False)

    def test_negative_five_mul(self):
        res = area(10, -5)
        self.assertEqual(res, False)

    def test_negative_both_mul(self):
        res = area(-10, -5)
        self.assertEqual(res, False)

    def test_negative_zero_mul(self):
        res = area(-10, 0)
        self.assertEqual(res, False)

    def test_zero_sum(self):
        res = perimeter(10, 0, 5)
        self.assertEqual(res, False)

    def test_one_five_sum(self):
        res = perimeter(10, 1, 5)
        self.assertEqual(res, 16)

    def test_equiangular_sum(self):
        res = perimeter(10, 10, 5)
        self.assertEqual(res, 25)

    def test_equilateral_sum(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_one_negative_five_sum(self):
        res = perimeter(10, 1, -5)
        self.assertEqual(res, False)

    def test_negative_one_five_sum(self):
        res = perimeter(10, -1, -5)
        self.assertEqual(res, False)

    def test_negative_all_mul(self):
        res = area(-10, -1, -5)
        self.assertEqual(res, False)

    def test_negative_zero_sum(self):
        res = perimeter(-10, 1, 0)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
