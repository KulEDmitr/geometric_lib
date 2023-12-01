import unittest

from ISRPO_Unittests.src.triangle import tri_area
from ISRPO_Unittests.src.triangle import tri_perimeter


class TriangleTestCase(unittest.TestCase):
    def test_tri_area_zero_side(self):
        res = tri_area(0, 10)
        self.assertEqual(res, 0.0)

    def test_tri_area_zero_height(self):
        res = tri_area(10, 0)
        self.assertEqual(res, 0.0)

    def test_tri_perimeter_zero_sides(self):
        res = tri_perimeter(0, 0, 0)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_perimeter(self):
        res = tri_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_tri_area_neg_side(self):
        res = tri_area(-3, 9)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_area_neg_height(self):
        res = tri_area(9, -7)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_perimeter_neg_all_sides(self):
        res = tri_perimeter(-3, -4, -5)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_area_no_existance(self):
        res = tri_perimeter(1, 2, 3)
        self.assertEqual(res, "Wrong input parameters")


if __name__ == '__main__':
    unittest.main()
