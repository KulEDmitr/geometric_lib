import unittest

from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10)
        self.assertEqual(res, 314.15926535897932384626433832795)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_normal_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586476925286766559)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-10)
        self.assertEqual(res, 314.15926535897932384626433832795)

    def test_negative_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, 62.83185307179586476925286766559)

    def test_huge_perimeter(self):
        res = perimeter(12738495757192482917)
        self.assertEqual(res, 80038329377161309809.304811729752)

    def test_huge_area(self):
        res = area(878545256984)
        self.assertEqual(res, 2424812429870383277813911.2874157)

    def test_unparsable_area(self):
        res = area("10u81h")
        self.assertEqual(res, 314.15926535897932384626433832795)

    def test_unparsable_perimeter(self):
        res = perimeter("10nfk34ngi")
        self.assertEqual(res, 62.83185307179586476925286766559)

    def test_double_area(self):
        res = area(0.1)
        self.assertLessEqual(abs(res - 0.031415926535897932384626433832), 0.000000001)

    def test_double_perimeter(self):
        res = perimeter(0.1)
        self.assertLessEqual(abs(res - 0.6283185307179586476925286766), 0.000000001)

