import unittest
from rectangle import area
from rectangle import perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10, 1)
        self.assertEqual(res, 10)
        res = area(10, 10)
        self.assertEqual(res, 100)
        res = area(15, 3)
        self.assertEqual(res, 45)
        res = area(4, 7)
        self.assertEqual(res, 28)

    def test_big_area(self):
        res = area(1000000000000000000, 0)
        self.assertEqual(res, 0)
        res = area(123456789, 123456789)
        self.assertEqual(res, 15241578750190521)
        res = area(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)
        res = area(48239492949, 2345)
        self.assertEqual(res, 113121610965405)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -2, 100)
        self.assertRaises(ValueError, area, -2000, -1100)
        self.assertRaises(ValueError, area, -234564, 100234362535)
        self.assertRaises(ValueError, area, -5435362, -234600)
        self.assertRaises(ValueError, area, 0, 1)
        self.assertRaises(ValueError, area, 1, 0)

    def test_wrong_type_area(self):
        self.assertRaises(TypeError, area, [-2], [100])
        self.assertRaises(TypeError, area, [123], [100])
        self.assertRaises(TypeError, area, "123", "car")
        self.assertRaises(TypeError, area, True, False)


class RectanglePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
        res = perimeter(15, 3)
        self.assertEqual(res, 36)
        res = perimeter(4, 7)
        self.assertEqual(res, 22)

    def test_big_perimetr(self):
        res = perimeter(1000000000000000000, 1)
        self.assertEqual(res, 2000000000000000002)
        res = perimeter(123456789, 123456789)
        self.assertEqual(res, 493827156)
        res = perimeter(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 4000000000000000000)
        res = perimeter(48239492949, 2345)
        self.assertEqual(res, 96478990588)

    def test_wrong_value_perimetr(self):
        self.assertRaises(ValueError, perimeter, -2, 100)
        self.assertRaises(ValueError, perimeter, -2000, -1100)
        self.assertRaises(ValueError, perimeter, -234564, 100234362535)
        self.assertRaises(ValueError, perimeter, -5435362, -234600)
        self.assertRaises(ValueError, perimeter, 0, 1)
        self.assertRaises(ValueError, perimeter, 1, 0)

    def test_wrong_type_perimetr(self):
        self.assertRaises(TypeError, perimeter, [-2], [100])
        self.assertRaises(TypeError, perimeter, [123], [100])
        self.assertRaises(TypeError, perimeter, "123", "car")
        self.assertRaises(TypeError, perimeter, True, False)
