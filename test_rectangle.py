from rectangle import area, perimeter

import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_mul1(self):
        res = area(3, 4)
        self.assertEqual(res, 12)
        
    def test_mul2(self):
        res = area(-9, 5)
        self.assertEqual(res, 0)

    def test_add1(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_add2(self):
        res = perimeter(8, -5)
        self.assertEqual(res, 0)
