import unittest
from triangle import area, perimeter

class TestTriangleModule(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 6), 12.0)
        self.assertEqual(area(7, 5), 17.5)
        self.assertEqual(area(0, 8), 0)
        self.assertEqual(area(3, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 12, 13), 30)
        self.assertEqual(perimeter(0, 8, 6), 14)
        self.assertEqual(perimeter(3, 0, 4), 7)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 6), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(4, 0), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()
