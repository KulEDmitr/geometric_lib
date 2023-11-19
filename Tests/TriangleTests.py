import unittest
from triangle import area
from triangle import perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(0, 3)
        self.assertEqual(res, 0)
        res = area(3, 0)
        self.assertEqual(res, 0)
        res = area(15, 3)
        self.assertEqual(res, 22.5)

    def test_big_area(self):
        res = area(10000000000000000000000000000, 300000)
        self.assertEqual(res, 10000000000000000000000000000 * 300000 / 2)
        res = area(9876543210, 1234567890)
        self.assertEqual(res, 9876543210 * 1234567890 / 2)
        res = area(100000000000000000000000000, 10000000000000000000000000000000)
        self.assertEqual(res, 100000000000000000000000000 * 10000000000000000000000000000000 / 2)

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


class TrianglePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        res = perimeter(28, 3, 30)
        self.assertEqual(res, 61)
        res = perimeter(15, 18, 7)
        self.assertEqual(res, 40)

    def test_big_perimetr(self):
        res = perimeter(1000000000000000000, 1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 3000000000000000000)
        res = perimeter(1000000000000000000, 1000000000000000000, 1)
        self.assertEqual(res, 2000000000000000001)
        res = perimeter(1234567890, 9876543210, 1000000000)
        self.assertEqual(res, 1234567890 + 9876543210 + 1000000000)

    def test_wrong_value_perimetr(self):
        with self.assertRaises(ValueError):
            perimeter(-124, 10, -1)
        with self.assertRaises(ValueError):
            perimeter(-4.2, 3.8, -10)
        with self.assertRaises(ValueError):
            perimeter(-10000000000000000000000000000, 14, 4215)

    def test_wrong_type_perimetr(self):
        with self.assertRaises(TypeError):
            perimeter("sdvg", "okr", "shiz")
        with self.assertRaises(TypeError):
            perimeter([123, 423, 124], [41, 5], [82, 19])
        with self.assertRaises(TypeError):
            perimeter(False, True, True)