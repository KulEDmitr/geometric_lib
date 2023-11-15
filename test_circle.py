import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_area(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 25.132741228718345)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            area('a')

    def test_less_than_0_area(self):
        res = area(-45)
        self.assertEqual(res, "Error")

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a')

    def test_less_than_0_perimeter(self):
        res = perimeter(-19)
        self.assertEqual(res, "Error")
