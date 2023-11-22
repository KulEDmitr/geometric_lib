import unittest, math
from circle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, False)

    def test_one_mul(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_ten_mul(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_negative_one_mul(self):
        res = area(-1)
        self.assertEqual(res, False)

    def test_negative_ten_mul(self):
        res = area(-10)
        self.assertEqual(res, False)

    def test_zero_sum(self):
        res = perimeter(0)
        self.assertEqual(res, False)

    def test_one_sum(self):
        res = perimeter(1)
        self.assertEqual(res, math.pi)

    def test_ten_sum(self):
        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)

    def test_negative_one_sum(self):
        res = perimeter(-1)
        self.assertEqual(res, False)

    def test_negative_ten_sum(self):
        res = perimeter(-10)
        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()
