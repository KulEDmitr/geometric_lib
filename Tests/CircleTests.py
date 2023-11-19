import unittest
import math
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(0)
        ans = math.pi * 0
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)
        res = area(100)
        ans = math.pi * 10000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)
        res = area(45)
        ans = math.pi * 2025
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_big_area(self):
        res = area(100000000000000000000)
        ans = math.pi * 10000000000000000000000000000000000000000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)
        res = area(1000000000000000000)
        ans = math.pi * 1000000000000000000000000000000000000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)
        res = area(1234567890)
        ans = math.pi * 1234567890 * 1234567890
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

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


class CirclePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(15)
        self.assertEqual(res, math.pi * 30)
        res = perimeter(100)
        self.assertEqual(res, math.pi * 200)
        res = perimeter(0)
        self.assertEqual(res, math.pi * 0)

    def test_big_perimetr(self):
        res = perimeter(200000000000000000001)
        self.assertEqual(res, math.pi * 400000000000000000002)
        res = perimeter(1234567890)
        self.assertEqual(res, math.pi * 1234567890 * 2)
        res = perimeter(1000000000000000000000)
        self.assertEqual(res, math.pi * 2000000000000000000000)

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
