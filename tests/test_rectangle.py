import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_large_number_area(self):
        res = area(1_567_234_812, 2_745_273_462)
        self.assertEqual(res, 4_302_488_138_106_159_144)

    def test_float_area(self):
        res = area(1_567.234_812, 2_745.273_462)
        self.assertTrue(abs(res - 4_302_488.138_106_159_144) <= 10 ** -6)

    def test_1_perimeter(self):
        res = perimeter(2, 4)
        self.assertEqual(res, 12)

    def test_2_perimeter(self):
        res = perimeter(12345, 32431)
        self.assertEqual(res, 89552)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.4, 5.7)
        self.assertEqual(res, 16.2)

    def test_str_1_area(self):
        self.assertRaises(TypeError, area, 'a', 4)

    def test_str_2_area(self):
        self.assertRaises(TypeError, area, 'a', '死')

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -4, 2)

    def test_str_1_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'a', 3)

    def test_str_2_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'a', '死')

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -4, 3)


if __name__ == "__main__":
    unittest.main()
