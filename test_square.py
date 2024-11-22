import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res2 = area(0)
        self.assertEqual(res2, 0)


    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
        
        res3 = area(15)
        self.assertEqual(res3, 225)
        
        res2 = area(1)
        self.assertEqual(res2, 1)

    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
        
        res2 = perimeter(1)
        self.assertEqual(res2, 4)
        
        res3 = perimeter(100)
        self.assertEqual(res3, 400)