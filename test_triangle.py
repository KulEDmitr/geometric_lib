import unittest
from triangle import area_triangle
from triangle import perimeter_triangle

class TriangleTestCase(unittest.TestCase):
    def test_0_mul(self):
        result = area_triangle(7, 8)
        self.assertEqual(result, 30)

    def test_1_mul(self):
        result = area_triangle(10, 5)
        self.assertEqual(result, 25)

    def test_2_mul(self):
        result = area_triangle(7.5, 3.5)
        self.assertEqual(result, 13.125)

    def test_3_mul(self):
        result = perimeter_triangle(0, 0, 0)
        self.assertEqual(result, 0)


    def test_4_mul(self):
        result = perimeter_triangle(10, 4, 8)
        self.assertEqual(result, 22)


    def test_five_mul(self):
        result = perimeter_triangle(34.23, 42.34, 23.43)
        self.assertEqual(result, 100)
