import unittest
import rectangle


class CircleTests(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)
    
    def test_big_nums(self):
        res = rectangle.area(10**20, 8**15)
        self.assertEqual(res, 10**20 * 8**15)


if __name__ == "__main__":
    unittest.main()
