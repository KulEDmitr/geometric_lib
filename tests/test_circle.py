import unittest
import circle
import math


class CircleTests(unittest.TestCase):
    def test_area(self):
        res = circle.area(10)
        self.assertEqual(res, math.pi * 100)

    def test_perimeter(self):
        res = circle.perimeter(10)
        self.assertEqual(res, math.pi * 20)

    def test_big_nums(self):
        res = circle.area(10**10)
        self.assertEqual(res, 10**20 * math.pi)


if __name__ == "__main__":
    unittest.main()
