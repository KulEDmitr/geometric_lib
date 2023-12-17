import unittest
from math import pi
from circle import area , perimeter

class RectangleTestCase(unittest.TestCase):
    def test_0_area(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_1_area(self):
        res = area(100_000)
        self.assertEqual(res,math.pi*100_000*100_000)
    @unittest.expectedFailure
    def test_2_area(self):
        res = area('a')
        self.assertEqual(res,TypeError)

    def test_0_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(100_000)
        self.assertEqual(res,2*math.pi*100_000)
    @unittest.expectedFailure
    def test_2_perimeter(self):
        res = perimeter('a')
        self.assertEqual(res,TypeError)