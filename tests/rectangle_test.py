import unittest
from lib.rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_yes(self):
        res = area(4, 7)
        self.assertEqual(res, 28)

    def test_rectangle_area_real_numbers(self):
        res = area(4.25, 7.36)
        self.assertEqual(res, 31.28)

    def test_rectangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_yes(self):
        res = perimeter(4, 7)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_real_numbers(self):
        res = perimeter(4.25, 7.36)
        self.assertEqual(res, 23.22)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(4, 0)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()