from math import pi
import unittest
from geometric_lib import circle


class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle.area(2), pi * 4)
        with self.assertRaises(ValueError):
            circle.area(-1)
        with self.assertRaises(TypeError):
            circle.area([12, 45])
        with self.assertRaises(TypeError):
            circle.area("qwerty")

    def test_perimeter(self):
        self.assertEqual(circle.perimeter(4), pi * 8)
        with self.assertRaises(ValueError):
            circle.perimeter(-1)
        with self.assertRaises(TypeError):
            circle.perimeter([12, 45])
        with self.assertRaises(TypeError):
            circle.perimeter("qwerty")
