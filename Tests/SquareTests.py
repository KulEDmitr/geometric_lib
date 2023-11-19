import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(13)
        self.assertEqual(res, 169)
        res = area(0)
        self.assertEqual(res, 0)
        res = area(45)
        self.assertEqual(res, 2025)

    def test_big_area(self):
        res = area(1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)
        res = area(1234567890)
        self.assertEqual(res, 1234567890 * 1234567890)
        res = area(987543210)
        self.assertEqual(res, 987543210 * 987543210)

    def test_wrong_value_area(self):
        with self.assertRaises(ValueError):
            area(-124)
        with self.assertRaises(ValueError):
            area(-4.2)
        with self.assertRaises(ValueError):
            area(-10000000000000000000000000000)

    def test_wrong_type_area(self):
        with self.assertRaises(TypeError):
            area("okr")
        with self.assertRaises(TypeError):
            area([541, 124])
        with self.assertRaises(TypeError):
            area(True)


class SquarePerimetrTestCase(unittest.TestCase):

    def test_perimetr(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
        res = perimeter(0)
        self.assertEqual(res, 0)
        res = perimeter(100)
        self.assertEqual(res, 400)

    def test_big_perimetr(self):
        res = perimeter(1000000000000000000)
        self.assertEqual(res, 4000000000000000000)
        res = perimeter(1234567890)
        self.assertEqual(res, 4938271560)
        res = perimeter(9876543210)
        self.assertEqual(res, 9876543210 * 4)

    def test_wrong_value_perimetr(self):
        with self.assertRaises(ValueError):
            perimeter(-124)
        with self.assertRaises(ValueError):
            perimeter(-4.2)
        with self.assertRaises(ValueError):
            perimeter(-10000000000000000000000000000)

    def test_wrong_type_perimetr(self):
        with self.assertRaises(TypeError):
            perimeter("sdvg")
        with self.assertRaises(TypeError):
            perimeter([123, 423, 124])
        with self.assertRaises(TypeError):
            perimeter(False)