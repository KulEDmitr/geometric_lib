import unittest
import math
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)
        res = area(100)
        self.assertEqual(res, math.pi * 10000)
        res = area(15)
        self.assertEqual(res, math.pi * 225)
        res = area(43)
        self.assertEqual(res, math.pi * 1849)

    def test_big_area(self):
        res = area(1000000000000000000)
        self.assertEqual(res, math.pi * 1000000000000000000000000000000000000)
        res = area(123456789)
        self.assertEqual(res, math.pi * 15241578750190521)
        res = area(1000000000000000000)
        self.assertEqual(res, math.pi * 1000000000000000000000000000000000000)
        res = area(48239492949)
        self.assertEqual(res, math.pi * 48239492949 * 48239492949)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -2000)
        self.assertRaises(ValueError, area, -234564)
        self.assertRaises(ValueError, area, -5435362)
        self.assertRaises(ValueError, area, 0)

    def test_wrong_type_area(self):
        self.assertRaises(TypeError, area, [-2])
        self.assertRaises(TypeError, area, [123])
        self.assertRaises(TypeError, area, "car")
        self.assertRaises(TypeError, area, True)


class CirclePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)
        res = perimeter(200)
        self.assertEqual(res, math.pi * 400)
        res = perimeter(15)
        self.assertEqual(res, math.pi * 30)
        res = perimeter(4)
        self.assertEqual(res, math.pi * 8)

    def test_big_perimetr(self):
        res = perimeter(2000000000000000001)
        self.assertEqual(res, math.pi * 2000000000000000001 * 2)
        res = perimeter(123456789)
        self.assertEqual(res, math.pi * 123456789 * 2)
        res = perimeter(1000000000000000000)
        self.assertEqual(res, math.pi * 1000000000000000000 * 2)
        res = perimeter(48239492949)
        self.assertEqual(res, math.pi * 48239492949 * 2)

    def test_wrong_value_perimetr(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -2000)
        self.assertRaises(ValueError, perimeter, -234564)
        self.assertRaises(ValueError, perimeter, -5435362)
        self.assertRaises(ValueError, perimeter, 0)

    def test_wrong_type_perimetr(self):
        self.assertRaises(TypeError, perimeter, [-2])
        self.assertRaises(TypeError, perimeter, [123])
        self.assertRaises(TypeError, perimeter, "car")
        self.assertRaises(TypeError, perimeter, True)
