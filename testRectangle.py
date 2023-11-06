import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_b(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_both(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    # def test_area_str_mul_a(self):
    #     res = area("10", 2)
    #     self.assertNotEqual(res, "1010")
    #
    # def test_area_str_mul_b(self):
    #     res = area(2, "10")
    #     self.assertNotEqual(res, "1010")

    def test_perimeter_zero_a(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_zero_b(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_zero_both(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_mul(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)


if __name__ == '__main__':
    unittest.main()
