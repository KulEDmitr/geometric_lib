import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_yes(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_square_area_no(self):
        res = area(-3)
        self.assertEqual(res, 'The side of a square cannot be negative')

    def test_square_area_real_numbers(self):
        res = area(3.45)
        self.assertEqual(res, 11.902500000000002)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_yes(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_perimeter_no(self):
        res = perimeter(-3)
        self.assertEqual(res,'The side of a square cannot be negative')

    def test_square_perimeter_real_numbers(self):
        res = perimeter(3.45)
        self.assertEqual(res, 13.8)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()