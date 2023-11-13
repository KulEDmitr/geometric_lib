import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100)
        res = area(100)
        self.assertEqual(res, 10000)
        res = area(15)
        self.assertEqual(res, 225)
        res = area(43)
        self.assertEqual(res, 1849)

    def test_big_area(self):
        res = area(1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)
        res = area(123456789)
        self.assertEqual(res, 15241578750190521)
        res = area(1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)
        res = area(48239492949)
        self.assertEqual(res, 2327048679976620716601)

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


class SquarePerimetrTestCase(unittest.TestCase):

    def test_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
        res = perimeter(20)
        self.assertEqual(res, 80)
        res = perimeter(15)
        self.assertEqual(res, 60)
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_big_perimetr(self):
        res = perimeter(2000000000000000001)
        self.assertEqual(res, 8000000000000000004)
        res = perimeter(123456789)
        self.assertEqual(res, 493827156)
        res = perimeter(1000000000000000000)
        self.assertEqual(res, 4000000000000000000)
        res = perimeter(48239492949)
        self.assertEqual(res, 192957971796)

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
