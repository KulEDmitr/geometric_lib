import unittest
import square


class CircleTests(unittest.TestCase):
    def test_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_big_nums(self):
        res = square.area(10**20)
        self.assertEqual(res, 20**20)


if __name__ == "__main__":
    unittest.main()
