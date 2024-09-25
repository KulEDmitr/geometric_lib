import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(14)
        self.assertEqual(res, 56)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            area('a')

    # def test_less_than_0_area(self):
    #     res = area(-5)
    #     self.assertEqual(res, "Error")

    # def test_str_perimeter(self):
    #     with self.assertRaises(TypeError):
    #         perimeter('a')

    # def test_less_than_0_perimeter(self):
    #     res = perimeter(-10)
    #     self.assertEqual(res, "Error")