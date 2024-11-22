import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
        res2 = area(0, 0)
        self.assertEqual(res2, 0)
        
        res3 = area(0, 10)
        self.assertEqual(res3, 0)

    def test_rectangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        
        res2 = area(1, 1)
        self.assertEqual(res2, 1)
        
        res3 = area(1, 100)
        self.assertEqual(res3, 100)

    def test_rectangle_perimeter(self):
        res = perimeter(10, 15)
        self.assertEqual(res, 50)
        
        res2 = perimeter(1, 2)
        self.assertEqual(res2, 6)
        
        res3 = perimeter(1, 100)
        self.assertEqual(res3, 202)