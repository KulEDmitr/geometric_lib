import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, False)

    def test_one_mul(self):
        res = area(10, 1)
        self.assertEqual(res, 10)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

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
        res = perimeter(10, 0)
        self.assertEqual(res, False)

    def test_one_sum(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)

    def test_square_sum(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_one_sum(self):
        res = perimeter(10, -1)
        self.assertEqual(res, False)

    def test_negative_five_sum(self):
        res = perimeter(10, -5)
        self.assertEqual(res, False)

    def test_negative_both_mul(self):
        res = area(-10, -5)
        self.assertEqual(res, False)

    def test_negative_zero_sum(self):
        res = perimeter(-10, 0)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
