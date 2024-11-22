import unittest
from geometric_lib import square


class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square.area(2), 4)
        with self.assertRaises(ValueError):
            square.area(-1)
        with self.assertRaises(TypeError):
            square.area([12, 45])
        with self.assertRaises(TypeError):
            square.area("qwerty")

    def test_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)
        with self.assertRaises(ValueError):
            square.perimeter(-1)
        with self.assertRaises(TypeError):
            square.perimeter([12, 45])
        with self.assertRaises(TypeError):
            square.perimeter("qwerty")

