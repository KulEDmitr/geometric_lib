import unittest
import triangle


class CircleTests(unittest.TestCase):
    def test_area(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = triangle.perimeter(10, 5, 14)
        self.assertEqual(res, 29)

    def test_big_nums(self):
        res = triangle.area(10**20, 8**15)
        self.assertEqual(res, 10**20 * 8**15 / 2)


if __name__ == "__main__":
    unittest.main()
