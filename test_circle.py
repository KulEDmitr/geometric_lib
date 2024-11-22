import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_mul(self):
        res = area(1)
        self.assertEqual(res, 3.14159)
        
        res2 = area(10)
        self.assertEqual(res2,  31.41592)
    def test_circle_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 6.28318)
        
        res2 = perimeter(2)
        self.assertEqual(res2, 12.56637)
