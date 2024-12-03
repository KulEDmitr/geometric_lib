from triangle import area, perimeter

import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0.0)

    def test_mul1(self):
        res = area(10, -10)
        self.assertEqual(res, 0)
        
    def test_mul2(self):
        res = area(3, 4)
        self.assertEqual(res, 6.0)

    def test_add1(self):
        res = perimeter(10, 4, 6)
        self.assertEqual(res, 20)

    def test_add2(self):
        res = perimeter(3, -5, 5)
        self.assertEqual(res, 0)
