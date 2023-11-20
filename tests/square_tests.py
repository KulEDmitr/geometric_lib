import sys
sys.path.append('../')
from square import *
import unittest

class TestSquareFunctions(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(2.5), 2.5 * 2.5)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_large_side(self):
        self.assertEqual(area(100), 100 * 100)

    def test_area_negative_side(self):
        self.assertEqual(area(-2.5), -2.5 * -2.5)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(2.5), 4 * 2.5)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_large_side(self):
        self.assertEqual(perimeter(100), 4 * 100)

    def test_perimeter_negative_side(self):
        self.assertEqual(perimeter(-2.5), 4 * -2.5)

    def test_area_perimeter_relation(self):
        side_a = 2.5
        square_area = area(side_a)
        square_perimeter = perimeter(side_a)
        self.assertAlmostEqual(square_area / square_perimeter, side_a / 4)

    def test_perimeter_area_relation(self):
        side_a = 2.5
        square_area = area(side_a)
        square_perimeter = perimeter(side_a)
        self.assertAlmostEqual(square_perimeter / square_area, 4 / side_a)
        
    def test_area_output(self):
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter_output(self):
        self.assertEqual(perimeter(2.5), 10.0)

    def test_area_invalid_input(self): 
        with self.assertRaises(TypeError):
            area('a')

    def test_perimeter_invalid_input(self): 
        with self.assertRaises(TypeError):
            perimeter('a')

if __name__ == '__main__':
    unittest.main()
