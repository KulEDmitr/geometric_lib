import unittest

import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)
    
    def test_area_null(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, -4)
    
    def test_perimeter (self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
    
    def test_perimeter_null(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(0, -4)

    def test_invalid_parametrs(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        with self.assertRaises(TypeError):
            rectangle.area((1, 2), (3, 4))

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-2, 4)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-2, 8)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)
    
    def test_area_null(self):
        with self.assertRaises(ValueError):
            triangle.area(0, -4)
    
    def test_perimeter (self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_null(self):
        res = triangle.perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_invalid_parametrs(self):
        with self.assertRaises(TypeError):
            triangle.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        with self.assertRaises(TypeError):
            triangle.area((1, 2), (3, 4))
    
    def test_perimeter_null(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, 4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-2, 4, 6)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-2, 8)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_area_null(self):
        with self.assertRaises(ValueError):
            square.area(0)
    
    def test_perimeter (self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
    
    def test_perimeter_null(self):
        with self.assertRaises(ValueError):
            square.perimeter(0)

    def test_invalid_parametrs(self):
        with self.assertRaises(TypeError):
            square.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        with self.assertRaises(TypeError):
            square.area((1, 2), (3, 4))
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-2)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-2)
