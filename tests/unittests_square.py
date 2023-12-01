import unittest

from ISRPO_Unittests.src.square import sq_area
from ISRPO_Unittests.src.square import sq_perimeter


class SquareTestCase(unittest.TestCase):
    def test_sq_area_zero(self):
        res = sq_area(0)
        self.assertEqual(res, 0)

    def test_sq_area(self):
        res = sq_area(7)
        self.assertEqual(res, 49)

    def test_sq_perimeter_zero(self):
        res = sq_perimeter(0)
        self.assertEqual(res, 0)

    def test_sq_perimeter(self):
        res = sq_perimeter(7)
        self.assertEqual(res, 28)

    def test_sq_area_neg(self):
        res = sq_area(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_sq_perimeter_neg(self):
        res = sq_perimeter(-1)
        self.assertEqual(res, "Wrong input parameters")


if __name__ == '__main__':
    unittest.main()
