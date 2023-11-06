import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 40)


if __name__ == '__main__':
    unittest.main()
