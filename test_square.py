import unittest

from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase) :
    
    def test_zero_area(self):
        if (2 == 2):
            print("hello!")
        
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area1(self):
        
        res = area(5)
        self.assertEqual(res, 25)

    def test_area2(self):
        
        res = area(70)
        self.assertEqual(res, 4900)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter1(self):
        res = perimeter(6)
        self.assertEqual(res, 24)

    def test_perimeter2(self):
        res = perimeter(8)
        self.assertEqual(res, 32)


