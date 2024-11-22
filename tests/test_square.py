import unittest
from lib.square import area
from lib.square import perimeter

class TestSquare(unittest.TestCase):
    # Тест функции, ищущей площадь квадрата
    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(3), 9)
        self.assertEqual(area(100), 10000)
        self.assertEqual(area(20), 400)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(0.5), 0.25)

    def test_values_area(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -5)
        self.assertRaises(ValueError, area, -4)
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -100000)

    def test_types_area(self):
        self.assertRaises(TypeError, area, 'two')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, [16])
        self.assertRaises(TypeError, area, 'three')
        self.assertRaises(TypeError, area, 'a')
        self.assertRaises(TypeError, area, ['i', 5])
        self.assertRaises(TypeError, area, [3, 6])

    # Тест функции, ищущей периметр квадрата
    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(1000), 4000)
        self.assertEqual(perimeter(21), 84)
        self.assertEqual(perimeter(5), 20)

    def test_values_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -3377329)
        self.assertRaises(ValueError, perimeter, -4)
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -5)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'two')
        self.assertRaises(TypeError, perimeter, True)
        self.assertRaises(TypeError, perimeter, [16],)
        self.assertRaises(TypeError, perimeter, [3])
        self.assertRaises(TypeError, perimeter, 'a')
        self.assertRaises(TypeError, perimeter, 'i')
        self.assertRaises(TypeError, perimeter, [3, 5])


