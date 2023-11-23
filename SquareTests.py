import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area(self):
        a = area(0)
        self.assertEqual(a, 0)
        a = area(2)
        self.assertEqual(a, 2)
        a = area(5)
        self.assertEqual(a, 25)
        a = area(0.5)
        self.assertEqual(a, 0.25)

    def test_area_big_numbers(self):
        a = area(10 ** 10)
        self.assertEqual(a, 10 ** 20)
        a = area(111111111111)
        self.assertEqual(a, 12345679012320987654321)
        a = area(12341234)
        self.assertEqual(a, 152306056642756)
        a = area(12341234123412341234)
        self.assertEqual(a, 152306059688877178543891480857256642756)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        a = perimeter(0)
        self.assertEqual(a, 0)
        a = perimeter(1)
        self.assertEqual(a, 4)
        a = perimeter(100)
        self.assertEqual(a, 400)
        a = perimeter(13)
        self.assertEqual(a, 52)
        a = perimeter(0.3)
        self.assertEqual(a, 1.2)

    def test_perimeter_big_numbers(self):
        res = perimeter(10 ** 10)
        self.assertEqual(res, (10 ** 10) * 4)
        res = perimeter(12341234)
        self.assertEqual(res, 49364936)
        res = perimeter(11 ** 5)
        self.assertEqual(res, 11 ** 5 * 4)
        res = perimeter(33333333333333)
        self.assertEqual(res, 133333333333332)
