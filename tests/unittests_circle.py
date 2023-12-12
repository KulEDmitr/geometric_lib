import unittest

from src.circle import area
from src.circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(3)    
        self.assertEqual(res, 28.274333882308138)

    def test_circle_area_big(self):
        res = area(212345)
        self.assertEqual(res, 141655666324.37238)

    def test_circle_perimeter(self):
        res = perimeter(3)    
        self.assertEqual(res, 18.84955592153876)

    def test_circle_perimeter_big(self):
        res = perimeter(212345)    
        self.assertEqual(res, 1334202.9840530492)
        
    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)
        
    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_circle_area_neg(self):
        res = area(-1)
        self.assertEqual(res, "Incorrect input")

    def test_circle_perimeter_neg(self):
        res = perimeter(-1)
        self.assertEqual(res, "Incorrect input")


if __name__ == '__main__':
    unittest.main()
