import unittest
from circle import area, perimeter


class СircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    # def test_area_invalid_input(self):
    #     res = area(-10)
    #     self.assertGreaterEqual(res, 0, "Invalid input: area must be positive number")
    #     # self.assertEqual(res, 0)
    #
    # def test_perimeter_invalid_input(self):
    #     res = perimeter(-10)
    #     self.assertGreaterEqual(res, 0, "Invalid input: area must be positive number")
    #     # self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
