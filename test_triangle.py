import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_equilateral_triangle_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5",2 ,2)