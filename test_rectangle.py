import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 50)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5",2)