import unittest
from triangle import area
from triangle import perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10, 1)
        self.assertEqual(res, 5)
        res = area(10, 10)
        self.assertEqual(res, 50)
        res = area(15, 4)
        self.assertEqual(res, 30)
        res = area(4, 7)
        self.assertEqual(res, 14)

    def test_big_area(self):
        res = area(1000000000000000000, 3)
        self.assertEqual(res, 1500000000000000000)
        res = area(123456789, 12345678)
        self.assertEqual(res, 762078881953971)
        res = area(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 1000000000000000000*1000000000000000000/2)
        res = area(48239492949, 2346)
        self.assertEqual(res, 56584925229177)

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


class TrianglePerimetrTestCase(unittest.TestCase):
    def test_perimetr(self):
        res = perimeter(10, 1, 1)
        self.assertEqual(res, 12)
        res = perimeter(10, 10, 2)
        self.assertEqual(res, 22)
        res = perimeter(15, 3, 3)
        self.assertEqual(res, 21)
        res = perimeter(4, 7, 9)
        self.assertEqual(res, 20)

    def test_big_perimetr(self):
        res = perimeter(1000000000000000000, 1, 1234567)
        self.assertEqual(res, 1000000000001234568)
        res = perimeter(123456789, 123456789, 234156)
        self.assertEqual(res, 247147734)
        res = perimeter(1000000000000000000, 1000000000000000000, 324521)
        self.assertEqual(res, 2000000000000324521)
        res = perimeter(48239492949, 2345, 33424153)
        self.assertEqual(res, 48272919447)

    def test_wrong_value_perimetr(self):
        self.assertRaises(ValueError, perimeter, -2, 100, 123)
        self.assertRaises(ValueError, perimeter, -2000, -1100, 452)
        self.assertRaises(ValueError, perimeter, -234564, 100234362535, -342)
        self.assertRaises(ValueError, perimeter, -5435362, -234600, 32423)
        self.assertRaises(ValueError, perimeter, 0, 1, 1)
        self.assertRaises(ValueError, perimeter, 1, 0, 1)
        self.assertRaises(ValueError, perimeter, 1, 1, 0)

    def test_wrong_type_perimetr(self):
        self.assertRaises(TypeError, perimeter, [-2], [100], [234])
        self.assertRaises(TypeError, perimeter, [123], [100], [12345])
        self.assertRaises(TypeError, perimeter, "123", "car", "23")
        self.assertRaises(TypeError, perimeter, True, False, True)
