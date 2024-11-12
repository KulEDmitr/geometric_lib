import unittest
from circle import area_circle
from circle import perimeter_circle

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result = area_circle(0)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_circle(10)
        self.assertEqual(result, 314.1592653589793)

    def test_two_mul(self):
        result = area_circle(67.636)
        self.assertEqual(result, 14371.619275936122)

    def test_three_mul(self):
        result = perimeter_circle(0)
        self.assertEqual(result, 0)


    def test_four_mul(self):
        result = perimeter_circle(10)
        self.assertEqual(result, 62.83185307179586)

    def test_five_mul(self):
        result = perimeter_circle(67.636)
        self.assertEqual(result, 424.96952143639845)