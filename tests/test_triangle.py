import unittest
from triangle import area, perimeter


class TriangleTestArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(area(5, 2), 5)
        self.assertEqual(area(18, 9), 81)
        self.assertEqual(area(4, 0.8), 1.6)
    
    def test_zero_values(self):
        self.assertEqual(area(128, 0), 0)
        self.assertEqual(area(0, 218391), 0)
        self.assertEqual(area(0, 0), 0)

class TriangleTestPerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(perimeter(2, 5, 7), 14)
        self.assertEqual(perimeter(16, 18, 36), 70)
        self.assertEqual(perimeter(0.3, 0.5, 0.006), 0.806)
    
    def test_zero_values(self):
        self.assertEqual(perimeter(0, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()