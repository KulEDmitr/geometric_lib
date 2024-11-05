import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_mul(self):
        res = area(42)
        self.assertEqual(res, 1764)

        res2 = area(32)
        self.assertEqual(res2, 1024)

        res3 = area(1)
        self.assertEqual(res3, 1)

    def test_square_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

        res2 = perimeter(12)
        self.assertEqual(res2, 48)

        res3 = perimeter(885553535)
        self.assertEqual(res3, 3542214140)