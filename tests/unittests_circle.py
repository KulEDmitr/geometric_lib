import unittest

from ISRPO_Unittests.src.circle import circ_area
from ISRPO_Unittests.src.circle import circ_perimeter


class CircleTestCase(unittest.TestCase):
    def test_circ_area_zero(self):
        res = circ_area(0)
        self.assertEqual(res, 0.0)

    def test_circ_area(self):
        res = circ_area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_circ_perimeter_zero(self):
        res = circ_perimeter(0)
        self.assertEqual(res, 0.0)

    def test_circ_perimeter(self):
        res = circ_perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_circ_area_neg(self):
        res = circ_area(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_circ_perimeter_neg(self):
        res = circ_perimeter(-1)
        self.assertEqual(res, "Wrong input parameters")


if __name__ == '__main__':
    unittest.main()
