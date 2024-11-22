import unittest
from rectangle import area, perimeter


class RectangleTestArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(area(2, 5), 10)
        self.assertEqual(area(16, 18), 288)
        self.assertEqual(area(0.3, 0.5), 0.15)
    
    def test_zero_values(self):
        self.assertEqual(area(128, 0), 0)
        self.assertEqual(area(0, 218391), 0)
        self.assertEqual(area(0, 0), 0)

class RectangleTestPerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(perimeter(2, 5), 14)
        self.assertEqual(perimeter(16, 18), 68)
        self.assertEqual(perimeter(0.3, 0.5), 1.6)
    
    def test_zero_values(self):
        self.assertEqual(perimeter(0, 0), 0)


if __name__ == '__main__':
    unittest.main()