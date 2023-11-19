import unittest
from rectangle import area
from rectangle import perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(56743, 1)
        self.assertEqual(res, 56743)
        res = area(0, 157)
        self.assertEqual(res, 0)
        res = area(5647, 0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(1000000000000000000, 20)
        self.assertEqual(res, 20000000000000000000)
        res = area(1234567890, 9876543210)
        self.assertEqual(res, 1234567890 * 9876543210)
        res = area(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)

    def test_wrong_value_area(self):
        with self.assertRaises(ValueError):
            area(-124, 3)
        with self.assertRaises(ValueError):
            area(-4.2, 1)
        with self.assertRaises(ValueError):
            area(-10000000000000000000000000000, 65)

    def test_wrong_type_area(self):
        with self.assertRaises(TypeError):
            area("okr", "sdvg")
        with self.assertRaises(TypeError):
            area([541, 124], [8765544, 7654])
        with self.assertRaises(TypeError):
            area(True, False)


class RectanglePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        res = perimeter(1, 341)
        self.assertEqual(res, 684)
        res = perimeter(15, 34)
        self.assertEqual(res, 98)

    def test_big_perimetr(self):
        res = perimeter(1000000000000000000, 1)
        self.assertEqual(res, 2000000000000000002)
        res = perimeter(1234567890, 9876543210)
        self.assertEqual(res, (1234567890 + 9876543210) * 2)
        res = perimeter(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 4000000000000000000)

    def test_wrong_value_area(self):
        with self.assertRaises(ValueError):
            area(-124, 3)
        with self.assertRaises(ValueError):
            area(-4.2, 1)
        with self.assertRaises(ValueError):
            area(-10000000000000000000000000000, 65)

    def test_wrong_type_area(self):
        with self.assertRaises(TypeError):
            area("okr", "sdvg")
        with self.assertRaises(TypeError):
            area([541, 124], [8765544, 7654])
        with self.assertRaises(TypeError):
            area(True, False)