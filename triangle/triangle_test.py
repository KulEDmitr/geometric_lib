import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_yes(self):
        res = area(2, 8)
        self.assertEqual(res, 8)

    def test_triangle_area_no(self):
        res = area(2, -8)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_area_real_numbers(self):
        res = area(2.75, 8.6)
        self.assertEqual(res, 11.825)

    def test_triangle_area_zero(self):
        res = area(2, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_yes(self):
        res = perimeter(2, 8, 11)
        self.assertEqual(res, 21)

    def test_triangle_perimeter_no(self):
        res = perimeter(2, -8, 11)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_perimeter_real_numbers(self):
        res = perimeter(2.75, 8.6, 11)
        self.assertEqual(res, 22.35)

    def test_triangle_perimeter_zero(self):
        res = perimeter(2, 0, 8.59)
        self.assertEqual(res, 10.59)

if __name__ == '__main__':
    unittest.main()