import unittest

from src.triangle import area
from src.triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_tri_perimeter_zero_sides(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_tri_perimeter_neg_side(self):
        res = perimeter(-1, 1, 1)
        self.assertEqual(res, "Incorrect input")

    def test_tri_perimeter_neg_sides(self):
        res = perimeter(-1, -234, -11)
        self.assertEqual(res, "Incorrect input")

    def test_tri_area_neg_side(self):
        res = area(-1, 1)
        self.assertEqual(res, "Incorrect input")

    def test_tri_area_neg_height(self):
        res = area(1, -1)
        self.assertEqual(res, "Incorrect input")

    def test_tri_perimeter_neg_all_sides(self):
        res = perimeter(-1, -23243, -1234)
        self.assertEqual(res, "Incorrect input")
        
    def test_tri_area_zero_side(self):
        res = area(0, 3)
        self.assertEqual(res, 0.0)

    def test_tri_area_zero_height(self):
        res = area(3, 0)
        self.assertEqual(res, 0.0)

    def test_tri_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_tri_perimeter_big(self):
        res = perimeter(213245, 1234, 425342)
        self.assertEqual(res, 639821)

    def test_tri_area(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_tri_area_big(self):
        res = area(213245, 1234)
        self.assertEqual(res, 131572165)


if __name__ == '__main__':
    unittest.main()
