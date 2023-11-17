import unittest
from rectangle import area, perimeter

class TestRectangleModule(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(4.5, 2.5), 11.25)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(3, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(4.5, 2.5), 14.0)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(3, 0), 6)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 0), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
