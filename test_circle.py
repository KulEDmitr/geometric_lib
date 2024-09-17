import unittest
import math

from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase) :
    
    def test_zero_area(self):
        
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area1(self):
        
        res = area(5)
        self.assertEqual(res, 5 * 5 * math.pi)

    def test_area2(self):
        
        res = round(area(98), 2)
        self.assertEqual(res, round(98 * 98 * math.pi, 2))

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter1(self):
        res = perimeter(8)
        self.assertEqual(res, math.pi * 8 * 2)

    def test_perimeter2(self):
        res = perimeter(24)
        self.assertEqual(res, math.pi * 24 * 2)