import unittest
from rectangle import area_rectangle
from rectangle import perimeter_rectangle

class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        result = area_rectangle(0,13)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_rectangle(10,13)
        self.assertEqual(result, 130)

    def test_two_mul(self):
        result = area_rectangle(67.5,3.5)
        self.assertEqual(result, 236.25)

    def test_three_mul(self):
        result = perimeter_rectangle(0,0)
        self.assertEqual(result, 0)

    def test_four_mul(self):
        result = perimeter_rectangle(10,54)
        self.assertEqual(result, 128)

    def test_five_mul(self):
        result = perimeter_rectangle(67.636,42.364)
        self.assertEqual(result,220)