import unittest
from lib.circle import area
from lib.circle import perimeter

class TestCircle(unittest.TestCase):
    # Тест функции, ищущей площадь круга
    def test_area(self):
        self.assertEqual(area(6), 113.09733552923255)
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(100), 31415.926535897932)
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(20), 1256.6370614359173)
        self.assertEqual(area(15.5), 754.7676350249478)
        self.assertEqual(area(30), 2827.4333882308138)
        self.assertEqual(area(2), 12.566370614359172)

    def test_values_area(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -4000)
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -5.5)

    def test_types_area(self):
        self.assertRaises(TypeError, area, 'two')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, [16])
        self.assertRaises(TypeError, area, 'three')
        self.assertRaises(TypeError, area, 'a')
        self.assertRaises(TypeError, area, ['i', 5])
        self.assertRaises(TypeError, area, [3, 6])

    # Тест функции, ищущей периметр круга

    def test_perimeter(self):
        self.assertEqual(perimeter(6), 37.69911184307752)
        self.assertEqual(perimeter(3), 18.84955592153876)
        self.assertEqual(perimeter(100), 628.3185307179587)
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(20), 125.66370614359172)
        self.assertEqual(perimeter(15.5), 97.38937226128358)
        self.assertEqual(perimeter(30), 188.49555921538757)
        self.assertEqual(perimeter(2), 12.566370614359172)

    def test_values_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -4000)
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -5.5)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, 'two')
        self.assertRaises(TypeError, perimeter, True)
        self.assertRaises(TypeError, perimeter, [16])
        self.assertRaises(TypeError, perimeter, 'three')
        self.assertRaises(TypeError, perimeter, 'a')
        self.assertRaises(TypeError, perimeter, ['i', 5])
        self.assertRaises(TypeError, perimeter, [3, 6])
