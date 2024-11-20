import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(3, 5), 7.5)
        self.assertEqual(triangle.area(1, 2), 1.0)

        self.assertRaises(ValueError, triangle.area, -5, 1)
        self.assertRaises(ValueError, triangle.area, 5, -1)
        self.assertRaises(ValueError, triangle.area, -5, -1)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 5, 6), 14)
        self.assertEqual(triangle.perimeter(1, 2, 3), 6)

        self.assertRaises(ValueError, triangle.perimeter, -5, 1, 3)
        self.assertRaises(ValueError, triangle.perimeter, 5, -1, 3)
        self.assertRaises(ValueError, triangle.perimeter, -5, -1, -3)


if __name__ == '__main__':
    unittest.main()
