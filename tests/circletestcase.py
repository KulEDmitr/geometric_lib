import unittest
from geometric_lib.circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(10), 314.1592653589793)
        self.assertEqual(area(1), 3.141592653589793)
        self.assertEqual(area(18), 1017.8760197630929)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(0.123), 0.04752915525615998)

    def test_value_area(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -9)
        self.assertRaises(ValueError, area, -123)
        self.assertRaises(ValueError, area, -0.1412)

    def test_types_area(self):
        self.assertRaises(TypeError, area, [1, 2, 3])
        self.assertRaises(TypeError, area, "23")
        self.assertRaises(TypeError, area, "hello")

    def test_perimeter(self):
        self.assertEqual(perimeter(10), 62.83185307179586)
        self.assertEqual(perimeter(1), 6.283185307179586)
        self.assertEqual(perimeter(18), 113.09733552923255)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(0.123), 0.7728317927830891)

    def test_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -9)
        self.assertRaises(ValueError, perimeter, -123)
        self.assertRaises(ValueError, perimeter, -0.1412)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, [1, 2, 3])
        self.assertRaises(TypeError, perimeter, "23")
        self.assertRaises(TypeError, perimeter, "hello")

