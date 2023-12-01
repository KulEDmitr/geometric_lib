import unittest

from ISRPO_Unittests.src.rectangle import rect_area
from ISRPO_Unittests.src.rectangle import rect_perimeter


class RectangleTestCase(unittest.TestCase):
    def test_rect_area_zero(self):
        res = rect_area(10, 0)
        self.assertEqual(res, 0)

    def test_rect_area_square(self):
        res = rect_area(10, 10)
        self.assertEqual(res, 100)

    def test_rect_area_big_square(self):
        res = rect_area(10 ** 4, 10 ** 7)
        self.assertEqual(res, 100000000000)

    def test_rect_perimeter_zero(self):
        res = rect_perimeter(5, 0)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_perimeter_square(self):
        res = rect_perimeter(4, 4)
        self.assertEqual(res, 16)

    def test_rect_perimeter_big_square(self):
        res = rect_perimeter(1000000, 1000000)
        self.assertEqual(res, 4000000)

    def test_rect_area_neg_both(self):
        res = rect_area(-2, -1)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_area_neg_first(self):
        res = rect_area(-1, 10)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_area_neg_second(self):
        res = rect_area(10, -2)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_perimeter_neg_both(self):
        res = rect_perimeter(-4, -9)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_perimeter_neg_first(self):
        res = rect_perimeter(-9, 10)
        self.assertEqual(res, "Wrong input parameters")

    def test_rect_perimeter_neg_second(self):
        res = rect_perimeter(10, -5)
        self.assertEqual(res, "Wrong input parameters")


if __name__ == '__main__':
    unittest.main()
