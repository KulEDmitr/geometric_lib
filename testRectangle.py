import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)
        self.assertEqual(rectangle.area(1, 2), 2)

        self.assertRaises(ValueError, rectangle.area, -5, 1)
        self.assertRaises(ValueError, rectangle.area, 5, -1)
        self.assertRaises(ValueError, rectangle.area, -5, -1)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)
        self.assertEqual(rectangle.perimeter(1, 2), 6)

        self.assertRaises(ValueError, rectangle.perimeter, -5, 1)
        self.assertRaises(ValueError, rectangle.perimeter, 5, -1)
        self.assertRaises(ValueError, rectangle.perimeter, -5, -1)


if __name__ == '__main__':
    unittest.main()
