import math
import unittest
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(area(1), math.pi)
        self.assertEquals(area(5), math.pi * 5 * 5)
        self.assertEquals(area(0), 0)
        self.assertEquals(area(1.5), math.pi * 1.5 * 1.5)
        self.assertEquals(area(10 ** 9), math.pi * 10 ** 9 * 10 ** 9)

    def test_area_values(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -22)

    def test_area_type(self):
        self.assertRaises(TypeError, area, 'ten')
        self.assertRaises(TypeError, area, [21])
        self.assertRaises(TypeError, area, False)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEquals(perimeter(1), 2 * math.pi)
        self.assertEquals(perimeter(5), 2 * math.pi * 5)
        self.assertEquals(perimeter(0), 0)
        self.assertEquals(perimeter(1.5), 2 * math.pi * 1.5)
        self.assertEquals(perimeter(10 ** 9), 2 * math.pi * 10 ** 9)

    def test_perimeter_values(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -22)

    def test_perimeter_type(self):
        self.assertRaises(TypeError, perimeter, 'ten')
        self.assertRaises(TypeError, perimeter, [21])
        self.assertRaises(TypeError, perimeter, False)
