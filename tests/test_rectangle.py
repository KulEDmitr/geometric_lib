import unittest
from geometric_lib import rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle.area(2, 3), 6)
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)
        with self.assertRaises(ValueError):
            rectangle.area(3, -5)
        with self.assertRaises(ValueError):
            rectangle.area(-3, -5)
        with self.assertRaises(TypeError):
            rectangle.area([12, 45], 4)
        with self.assertRaises(TypeError):
            rectangle.area(4, [12, 45])
        with self.assertRaises(TypeError):
            rectangle.area([12, 45], [12, 45])
        with self.assertRaises(TypeError):
            rectangle.area("qwerty", 1)
        with self.assertRaises(TypeError):
            rectangle.area(1, "qwerty")
        with self.assertRaises(TypeError):
            rectangle.area("qwerty", "qwerty")

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 3), 10)
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, -5)
        with self.assertRaises(TypeError):
            rectangle.perimeter([12, 45], 4)
        with self.assertRaises(TypeError):
            rectangle.perimeter(4, [12, 45])
        with self.assertRaises(TypeError):
            rectangle.perimeter([12, 45], [12, 45])
        with self.assertRaises(TypeError):
            rectangle.perimeter("qwerty", 1)
        with self.assertRaises(TypeError):
            rectangle.perimeter(1, "qwerty")
        with self.assertRaises(TypeError):
            rectangle.perimeter("qwerty", "qwerty")