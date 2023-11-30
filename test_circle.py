import unittest
from circle import area
from circle import perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = area(10)
        self.assertEqual(res, 314.15926535897932384626433832795)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5")