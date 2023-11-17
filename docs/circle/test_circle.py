import unittest
from circle import area
from circle import perimeter
import math


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), math.pi*4*4)

    def test_pi_area(self):
         self.assertEqual(area(1), math.pi)

    def test_zero_area(self):
        self.assertEqual(area(0), 0)

    def test_fractional_area(self):
        self.assertEqual(area(5.5), math.pi*5.5*5.5)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -2)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 2*math.pi*5)

    def test_pi_perimeter(self):
        self.assertEqual(perimeter(1), 2*math.pi)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)

    def test_fractional_perimeter(self):
        self.assertEqual(perimeter(2.5), 2*math.pi*2.5)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3)

