import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertFalse(rectangle.area(0, 10) == 3)

    def test_default(self):
        self.assertEqual(rectangle.area(10, 10), 100)
        self.assertEqual(rectangle.area(5, 2), 10)
        self.assertFalse(rectangle.area(2, 3) == 7)
        self.assertEqual(rectangle.perimeter(10, 10), 40)
        self.assertEqual(rectangle.perimeter(5, 2), 14)
        self.assertFalse(rectangle.perimeter(2, 3) == 7)
