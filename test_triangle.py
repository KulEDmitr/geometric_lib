import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
        res2 = area(0, 0)
        self.assertEqual(res2, 0)
        
        res3 = area(0, 10)
        self.assertEqual(res3, 0)

    def test_triangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
        
        res2 = area(1, 1)
        self.assertEqual(res2, 0.5)
        
        res3 = area(1, 100)
        self.assertEqual(res3, 50)

    def test_triangle_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
        
        res2 = perimeter(1, 2, 3)
        self.assertEqual(res2, 0)
        
        res3 = perimeter(1, 4, 4)
        self.assertEqual(res3, 9)