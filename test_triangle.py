import unittest

from tringle import area
from tringle import perimeter

class TriangleTestCase(unittest.TestCase) :
    
    def test_zero_area(self):
        
        res = area(0, 5)
        self.assertEqual(res, 0)
    
    def test_area1(self):
        
        res = area(5, 2)
        self.assertEqual(res, 5)

    def test_area2(self):
        
        res = area(70, 4)
        self.assertEqual(res, 140)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter1(self):
        res = perimeter(4, 5, 8)
        self.assertEqual(res, 17)

    def test_perimeter2(self):
        res = perimeter(59, 62, 6)
        self.assertEqual(res, 127)


