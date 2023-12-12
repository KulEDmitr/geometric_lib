import unittest

from src.rectangle import area
from src.rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rect_area_zero_both(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
        
    def test_rect_area_zero_f(self):
        res = area(3, 0)
        self.assertEqual(res, 0)
        
    def test_rect_area_zero_s(self):
        res = area(0, 3)
        self.assertEqual(res, 0)

    def test_rect_perimeter_zero_both(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        
    def test_rect_perimeter_zero_f(self):
        res = perimeter(3, 0)
        self.assertEqual(res, 6)
        
    def test_rect_perimeter_zero_s(self):
        res = perimeter(0, 3)
        self.assertEqual(res, 6)

    def test_rect_area_neg_both(self):
        res = area(-1, -2)
        self.assertEqual(res, "Incorrect input")

    def test_rect_area_neg_f(self):
        res = area(-3, 4)
        self.assertEqual(res, "Incorrect input")

    def test_rect_area_neg_s(self):
        res = area(5, -6)
        self.assertEqual(res, "Incorrect input")

    def test_rect_perimeter_neg_both(self):
        res = perimeter(-7, -8)
        self.assertEqual(res, "Incorrect input")

    def test_rect_perimeter_neg_f(self):
        res = perimeter(-9, 10)
        self.assertEqual(res, "Incorrect input")

    def test_rect_perimeter_neg_s(self):
        res = perimeter(11, -12)
        self.assertEqual(res, "Incorrect input")

    def test_rect_area_square(self):
        res = area(3, 3)
        self.assertEqual(res, 9)

    def test_rect_area_big_square(self):
        res = area(10 ** 5, 10 ** 5)
        self.assertEqual(res, 10 ** 10)

    def test_rect_perimeter_square(self):
        res = perimeter(3, 3)
        self.assertEqual(res, 12)

    def test_rect_perimeter_big_square(self):
        res = perimeter(10 ** 5, 10 ** 5)
        self.assertEqual(res, 4 * 10 ** 5)


if __name__ == '__main__':
    unittest.main()
