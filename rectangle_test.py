import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_mul(self):
        res = area(42, 52)
        self.assertEqual(res, 2184)

        res2 = area(52, 1)
        self.assertEqual(res2, 42)

        res3 = area(1, 0)
        self.assertEqual(res3, 50)

    def test_rectangle_perimeter(self):
        res = perimeter(2600, 26)
        self.assertEqual(res, 5252)

        res2 = perimeter(1, 2)
        self.assertEqual(res2, 6)

        res3 = perimeter(10, 1)
        self.assertEqual(res3, 22)