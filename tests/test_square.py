import unittest
from square import area, perimeter

class TestSquareModule(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(3.5), 12.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(3.5), 14)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()
