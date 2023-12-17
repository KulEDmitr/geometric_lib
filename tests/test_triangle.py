import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 14)
        self.assertEqual(res, 0)
       
    def test_small_number_area(self):
        res = area(10, 74)
        self.assertEqual(res, 370)

    def test_large_number_area(self):
        res = area(1_567_234_812, 2_745_273_462)
        self.assertEqual(res, 2_151_244_069_053_079_552)

    def test_float_area(self):
        res = area(1_567.234_812, 2_745.273_462)
        self.assertTrue(abs(res - 2_151_244.069_053_079_552) <= 10 ** -6)

    def test_1_perimeter(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_2_perimeter(self):
        res = perimeter(32431, 71223, 87254)
        self.assertEqual(res, 190908)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.4, 1.5, 8.9)
        self.assertEqual(res, 12.8)

    def test_str_1_area(self):
        self.assertRaises(TypeError, area, 'a', 4)

    def test_str_2_area(self):
        self.assertRaises(TypeError, area, 'a', '死')

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -4, 2)

    def test_str_1_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'a', 3, 2)

    def test_str_2_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'a', '死', 2)

    def test_str_3_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'a', '死', 'c')

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -4, 3, -2)


if __name__ == "__main__":
    unittest.main()
