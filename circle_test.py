import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_mul(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

        res2 = area(2)
        self.assertEqual(res2, 12.566370614359172)

        res3 = area(3)
        self.assertEqual(res3, 28.274333882308138)

    def test_circle_perimeter(self):
        res = perimeter(52)
        self.assertEqual(res, 326.7256359733385)

        res2 = perimeter(1)
        self.assertEqual(res2, 6.283185307179586)

        res3 = perimeter(0)
        self.assertEqual(res3, 0)