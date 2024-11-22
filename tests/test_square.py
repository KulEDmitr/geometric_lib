import unittest
from square import area, perimeter


class SquareTestArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(16), 256)
        self.assertEqual(area(0.3), 0.09)
    
    def test_zero_values(self):
        self.assertEqual(area(0), 0)

class SquareTestPerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(16), 64)
        self.assertEqual(perimeter(0.3), 1.2)
    
    def test_zero_values(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()