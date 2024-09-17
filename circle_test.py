import unittest

from circle import *

class CircleTest(unittest.TestCase):

    def test_area_integers(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(3), math.pi * 3 * 3)
        self.assertEqual(area(15), math.pi * 15 * 15)

    def test_perimeter_integers(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(6), 2 * math.pi * 6)
        self.assertEqual(perimeter(18), 2 * math.pi * 18)

    def test_area_non_integers(self):
        self.assertEqual(area(0.3), math.pi * 0.3 * 0.3)
        self.assertEqual(area(1.25), math.pi * 1.25 * 1.25)

    def test_perimeter_non_integers(self):
        self.assertEqual(perimeter(4.6), 2 * math.pi * 4.6)
        self.assertEqual(perimeter(1.8), 2 * math.pi * 1.8)

    def test_area_processing_values(self):
        self.assertEqual(area('1'), "enter a number")
        self.assertEqual(area('p'), "enter a number")

    # в файле circle.py функция area научилась выводить 1 тип ошибки
    def test_area_processing_values_2(self):
        self.assertEqual(area(-19), "negative numbers are not allowed")
        self.assertEqual(area(-8.2), "negative numbers are not allowed")

    def test_perimeter_processing_values(self):
        self.assertEqual(perimeter('i'), "enter a number")
        self.assertEqual(perimeter(-8), "negative numbers are not allowed")

if __name__ == '__main__':
    unittest.main()