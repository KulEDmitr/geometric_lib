import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(area(1), 1)
        self.assertEquals(area(5), 25)
        self.assertEquals(area(0), 0)
        self.assertEquals(area(1.5), 1.5 * 1.5)
        self.assertEquals(area(10 ** 9), 10 ** 18)

    def test_area_values(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -22)

    def test_area_type(self):
        self.assertRaises(TypeError, area, 'ten')
        self.assertRaises(TypeError, area, [21])
        self.assertRaises(TypeError, area, False)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEquals(perimeter(1), 4 * 1)
        self.assertEquals(perimeter(5), 4 * 5)
        self.assertEquals(perimeter(0), 0)
        self.assertEquals(perimeter(1.5), 4 * 1.5)
        self.assertEquals(perimeter(10 ** 9), 4 * 10 ** 9)

    def test_perimeter_values(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -22)

    def test_perimeter_type(self):
        self.assertRaises(TypeError, perimeter, 'ten')
        self.assertRaises(TypeError, perimeter, [21])
        self.assertRaises(TypeError, perimeter, False)
