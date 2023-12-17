import unittest
from square import area, perimeter



class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(20), 400)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(0.4562), 0.20811844)
        self.assertEqual(area(2.5), 6.25)

    def test_value_area(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -10)
        self.assertRaises(ValueError, area, -0.14)
        self.assertRaises(ValueError, area, -9.87654321)

    def test_types_area(self):
        self.assertRaises(TypeError, area, '1')
        self.assertRaises(TypeError, area, "hello")
        self.assertRaises(TypeError, area, [1])

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(20), 80)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(0.4562), 1.8248)
        self.assertEqual(perimeter(2.5), 10)

    def test_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -10)
        self.assertRaises(ValueError, perimeter, -0.14)
        self.assertRaises(ValueError, perimeter, -9.87654321)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, '1')
        self.assertRaises(TypeError, perimeter, "hello")
        self.assertRaises(TypeError, perimeter, [1])

