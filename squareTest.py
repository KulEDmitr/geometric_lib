import unittest
import square


class SquareTest(unittest.TestCase):
    def test_zero_side(self):
        self.assertTrue(square.area(0) == 0)
        self.assertEqual(square.area(0), 0)
        self.assertFalse(square.area(0) == 3)

    def test_default(self):
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(5), 25)
        self.assertFalse(square.area(2) == 7)
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(5), 20)
        self.assertFalse(square.perimeter(2) == 7)
