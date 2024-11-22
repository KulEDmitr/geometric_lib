import unittest
from lib.rectangle import area
from lib.rectangle import perimeter

class TestRectangle(unittest.TestCase):
    # Тест функции, ищущей площадь прямоугольника
    def test_area(self):
        self.assertEqual(area(2, 4), 8)
        self.assertEqual(area(2, 5), 10)
        self.assertEqual(area(3, 5), 15)
        self.assertEqual(area(100, 20), 2000)
        self.assertEqual(area(1000, 500), 500000)
        self.assertEqual(area(1, 0.5), 0.5)
        self.assertEqual(area(0, 0), 0)

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

    # Тест функции, ищущей периметр прямоугольника
    def test_perimeter(self):
        self.assertEqual(perimeter(2, 4), 12)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(1, 4), 10)
        self.assertEqual(perimeter(10, 20), 60)
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(10000, 67), 20134)

    def test_values_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2, 5)
        self.assertRaises(ValueError, perimeter, -3, -5)
        self.assertRaises(ValueError, perimeter, 2, -4)
        self.assertRaises(ValueError, perimeter, -2, -1)
        self.assertRaises(ValueError, perimeter, 2, -5)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'two', 5)
        self.assertRaises(TypeError, perimeter, 2, True)
        self.assertRaises(TypeError, perimeter, [16], [10])
        self.assertRaises(TypeError, perimeter, 'three', 'four')
        self.assertRaises(TypeError, perimeter, 'a', 'b')
        self.assertRaises(TypeError, perimeter, 'i', 5)
        self.assertRaises(TypeError, perimeter, True, True)

