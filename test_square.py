import unittest
from square import area_square
from square import perimeter_square

class SquareTestCase(unittest.TestCase):

    def test_zero_mul(self):
        result = area_square(0)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_square(10)
        self.assertEqual(result, 100)


    def test_two_mul(self):
        result = area_square(7.5)
        self.assertEqual(result, 56.25)

    def test_three_mul(self):
        result = perimeter_square(0)
        self.assertEqual(result, 0)


    def test_four_mul(self):
        result = perimeter_square(10)
        self.assertEqual(result, 55)

    def test_five_mul(self):
        result = perimeter_square(17.25)
        self.assertEqual(result, 56)