import unittest
from triangle import area
from triangle import perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_a_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_h_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_zero_a_perimeter(self):
        res = perimeter(0, 5, 15)
        self.assertEqual(res, 20)

    def test_zero_b_perimeter(self):
        res = perimeter(10, 0, 30)
        self.assertEqual(res, 40)

    def test_zero_c_perimeter(self):
        res = perimeter(11, 13, 0)
        self.assertEqual(res, 24)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10, 20, 30)
        self.assertEqual(res, 60)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            area('a', 'a')

    def test_less_than_0_area(self):
        res = area(-45, 67)
        self.assertEqual(res, "Error")

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 'a', 'a')

    def test_less_than_0_perimeter(self):
        res = perimeter(-19, -3, -7)
        self.assertEqual(res, "Error")