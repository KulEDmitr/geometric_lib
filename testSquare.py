import unittest
import square


class Testsquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(3), 9)
        self.assertEqual(square.area(2), 4)

        self.assertRaises(ValueError, square.area, -5)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.perimeter(2), 8)

        self.assertRaises(ValueError, square.perimeter, -5)


if __name__ == '__main__':
    unittest.main()
