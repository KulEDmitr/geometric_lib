import unittest, math
from circle import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_small_number_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_large_number_area(self):
        res = area(1_567_234_812)
        self.assertEqual(res, 2_456_224_955_944_675_344 * math.pi)

    def test_float_area(self):
        res = area(1_567.234_812)
        self.assertTrue(abs(res - 2_456_224.955_944_675_344 * math.pi) <= 10 ** -6)

    def test_1_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 4 * math.pi)

    def test_2_perimeter(self):
        res = perimeter(47456)
        self.assertEqual(res, 94912 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.4)
        self.assertEqual(res, 4.8 * math.pi)

    def test_str_area(self):
        self.assertRaises(TypeError, area, 'a')

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -4)

    def test_str_perimeter(self):
        self.assertRaises(TypeError, perimeter, '死')

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -4)


if __name__ == "__main__":
    unittest.main()
