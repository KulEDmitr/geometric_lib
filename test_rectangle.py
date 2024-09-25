import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_b_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_a_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_b_perimeter(self):
        res = perimeter(20, 0)
        self.assertEqual(res, 40)

    def test_zero_a_perimeter(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    # def test_less_than_0_a_area(self):
    #     res = area(-5, 3)
    #     self.assertEqual(res, "Error")

    # def test_less_than_0_b_area(self):
    #     res = area(15, -9)
    #     self.assertEqual(res, "Error")

    # def test_less_than_0_a_perimeter(self):
    #     res = perimeter(-11, 54)
    #     self.assertEqual(res, "Error")

    # def test_less_than_0_b_perimeter(self):
    #     res = perimeter(11, -14)
    #     self.assertEqual(res, "Error")

    # def test_str_perimeter(self):
    #     with self.assertRaises(TypeError):
    #         perimeter('a', 'a')

    def test_str_area(self):
        with self.assertRaises(TypeError):
            area('a', 'a')