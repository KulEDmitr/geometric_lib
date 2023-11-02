import unittest
from triangle import area
from triangle import perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(area(1, 2), 1 * 2 / 2)
        self.assertEquals(area(5, 3), 5 * 3 / 2)
        self.assertEquals(area(0, 4), 0)
        self.assertEquals(area(1.5, 2.4), 1.5 * 2.4 / 2)
        self.assertEquals(area(10 ** 9, 10 ** 9 + 1), (10 ** 9) * (10 ** 9 + 1) / 2)

    def test_area_values(self):
        self.assertRaises(ValueError, area, -2, 3)
        self.assertRaises(ValueError, area, -22, 5)

    def test_area_type(self):
        self.assertRaises(TypeError, area, 'ten', 'five')
        self.assertRaises(TypeError, area, [21], [6])
        self.assertRaises(TypeError, area, False, True)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEquals(perimeter(1, 2 , 3), 1 + 2 + 3)
        self.assertEquals(perimeter(5, 1, 2), 5 + 1 + 2)
        self.assertEquals(perimeter(0, 4, 3), 7)
        self.assertEquals(perimeter(4, 0, 2), 6)
        self.assertEquals(perimeter(1.5, 2.4, 3.2), 1.5 + 2.4 + 3.2)
        self.assertEquals(perimeter(10 ** 9, 10 ** 9 + 2, 10 ** 9), 10 ** 9 + 10 ** 9 + 2 + 10 ** 9)

    def test_perimeter_values(self):
        self.assertRaises(ValueError, perimeter, -2, -1, 4)
        self.assertRaises(ValueError, perimeter, -22, -3, 2)

    def test_perimeter_type(self):
        self.assertRaises(TypeError, perimeter, 'ten', 'five', 'seven')
        self.assertRaises(TypeError, perimeter, [21], [34], [32])
        self.assertRaises(TypeError, perimeter, False, True, False)
