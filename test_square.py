import unittest
from square import perimeter
from square import area

class SquareTestCase(unittest.TestCase):
    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5")