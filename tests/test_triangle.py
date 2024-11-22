import unittest
from lib.triangle import area
from lib.triangle import perimeter

class TestTriangle(unittest.TestCase):
    # Тест функции поиска площади треугольника
    def test_area(self):
        self.assertEqual(area(5, 6), 15)
        self.assertEqual(area(50, 13), 325)
        self.assertEqual(area(230, 9), 1035)
        self.assertEqual(area(56, 230), 6440)
        self.assertEqual(area(4, 5), 10)
        self.assertEqual(area(4.25, 5), 10.625)
        self.assertEqual(area(12.75, 5.5), 35.0625)
        self.assertEqual(area(16, 88), 704)

    def test_values_area(self):
        self.assertRaises(ValueError, area, -2, 5)
        self.assertRaises(ValueError, area, -3, -5)
        self.assertRaises(ValueError, area, 2, -4)
        self.assertRaises(ValueError, area, -2, -1)
        self.assertRaises(ValueError, area, 2, -5)

    def test_types_area(self):
        self.assertRaises(TypeError, area, 'two', 5)
        self.assertRaises(TypeError, area, 2, True)
        self.assertRaises(TypeError, area, [16], [10])
        self.assertRaises(TypeError, area, 'three', 'four')
        self.assertRaises(TypeError, area, 'a', 'b')
        self.assertRaises(TypeError, area, 'i', 5)
        self.assertRaises(TypeError, area, True, True)

    # Тест функции поиска периметра треугольника
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 6, 5), 16)
        self.assertEqual(perimeter(50, 13, 44), 107)
        self.assertEqual(perimeter(230, 9, 230), 469)
        self.assertEqual(perimeter(56, 230, 230), 516)
        self.assertEqual(perimeter(4, 5, 4), 13)
        self.assertEqual(perimeter(4.25, 5, 4.5), 13.75)
        self.assertEqual(perimeter(12.75, 5.5, 12), 30.25)
        self.assertEqual(perimeter(16, 88, 79), 183)

    def test_values_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2, 5, 5)
        self.assertRaises(ValueError, perimeter, -3, -5, 0)
        self.assertRaises(ValueError, perimeter, 2, -4, 3)
        self.assertRaises(ValueError, perimeter, -2, -1, -3)
        self.assertRaises(ValueError, perimeter, 2, -5, 6)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'two', 5, 7)
        self.assertRaises(TypeError, perimeter, 2, True, 3)
        self.assertRaises(TypeError, perimeter, [16], [10], [4])
        self.assertRaises(TypeError, perimeter, 'three', 'four', 3)
        self.assertRaises(TypeError, perimeter, 'a', 'b', 66)
        self.assertRaises(TypeError, perimeter, 'i', 5, 1)
        self.assertRaises(TypeError, perimeter, True, True, False)
