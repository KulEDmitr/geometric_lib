import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0.5), 0.25)

    def test_area_zero_value(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(0.25), 1)



if __name__ == '__main__':
    unittest.main()
