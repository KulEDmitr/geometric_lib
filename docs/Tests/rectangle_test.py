import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(4, 5), 20)

    def test_area_zero_values(self):
        self.assertEqual(area(0, 3), 0)
        self.assertEqual(area(4, 0), 0)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(2, 4), 12)
        self.assertEqual(perimeter(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
