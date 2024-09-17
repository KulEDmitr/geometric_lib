import unittest

from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase) :
    
    def test_zero_area(self):
        
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perimeter1(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_zero_perimeter2(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area1(self):
        
        res = area(12, 10)
        self.assertEqual(res, 120)

    def test_area2(self):
        res = area(5, 12)
        self.assertEqual(res, 60)

    def test_perimeter1(self):
        res = perimeter(16, 4)
        self.assertEqual(res, 40)

    def test_perimeter1(self):
        res = perimeter(4, 6)
        self.assertEqual(res, 20)
