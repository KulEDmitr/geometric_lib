import unittest
from geometric_lib import triangle


class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle.area(2, 5), 5)
        with self.assertRaises(ValueError):
            triangle.area(-1, 3)
        with self.assertRaises(ValueError):
            triangle.area(1, -3)
        with self.assertRaises(ValueError):
            triangle.area(-1, -3)
        with self.assertRaises(TypeError):
            triangle.area([12, 45], 4)
        with self.assertRaises(TypeError):
            triangle.area(4, [12, 45])
        with self.assertRaises(TypeError):
            triangle.area([12, 45], [12, 45])
        with self.assertRaises(TypeError):
            triangle.area("qwerty", 1)
        with self.assertRaises(TypeError):
            triangle.area(1, "qwerty")
        with self.assertRaises(TypeError):
            triangle.area("qwerty", "qwerty")

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(2, 5, 3), 10)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 10, 2)
        with self.assertRaises(ValueError):
            triangle.perimeter(10, 2, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 3, 2)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, -3, 2)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 3, -2)
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, -3, -2)
        with self.assertRaises(TypeError):
            triangle.perimeter([12, 45], 4, 3)
        with self.assertRaises(TypeError):
            triangle.perimeter(4, [12, 45], 3)
        with self.assertRaises(TypeError):
            triangle.perimeter(4, 3, [12, 45])
        with self.assertRaises(TypeError):
            triangle.perimeter([12, 45], [12, 45], [12, 45])
        with self.assertRaises(TypeError):
            triangle.perimeter("qwerty", 1, 2)
        with self.assertRaises(TypeError):
            triangle.perimeter(1, "qwerty", 2)
        with self.assertRaises(TypeError):
            triangle.perimeter(1, 2, "qwerty")
        with self.assertRaises(TypeError):
            triangle.perimeter("qwerty", "qwerty", "qwerty")