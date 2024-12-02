import unittest
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        '''Valid rectangle area calculation.'''
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12, msg=f"Expected area to be 12, but got {res}")
    
    def test_area_null(self):
        '''Invalid rectangle area handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid dimensions (0, -4)."):
            rectangle.area(0, -4)
    
    def test_perimeter(self):
        '''Valid rectangle perimeter calculation.'''
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14, msg=f"Expected perimeter to be 14, but got {res}")
    
    def test_perimeter_null(self):
        '''Invalid rectangle perimeter handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid dimensions (0, -4)."):
            rectangle.perimeter(0, -4)

    def test_invalid_parametrs(self):
        '''Non-numeric rectangle area inputs.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric inputs ('a', 'b')."):
            rectangle.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        '''Tuple inputs for rectangle area.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for tuple inputs ((1, 2), (3, 4))."):
            rectangle.area((1, 2), (3, 4))

    def test_perimeter_negative(self):
        '''Negative dimensions for rectangle perimeter.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions (-2, 4)."):
            rectangle.perimeter(-2, 4)
    
    def test_area_negative(self):
        '''Negative dimensions for rectangle area.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions (-2, 8)."):
            rectangle.area(-2, 8)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        '''Valid triangle area calculation.'''
        res = triangle.area(3, 4)
        self.assertEqual(res, 6, msg=f"Expected area to be 6, but got {res}")
    
    def test_area_null(self):
        '''Invalid triangle area handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid dimensions (0, -4)."):
            triangle.area(0, -4)
    
    def test_perimeter(self):
        '''Valid triangle perimeter calculation.'''
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12, msg=f"Expected perimeter to be 12, but got {res}")
    
    def test_perimeter_null(self):
        '''Zero side length for triangle perimeter.'''
        res = triangle.perimeter(0, 4, 5)
        self.assertEqual(res, 9, msg=f"Expected perimeter to be 9, but got {res}")

    def test_invalid_parametrs(self):
        '''Non-numeric triangle area inputs.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric inputs ('a', 'b')."):
            triangle.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        '''Tuple inputs for triangle area.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for tuple inputs ((1, 2), (3, 4))."):
            triangle.area((1, 2), (3, 4))
    
    def test_perimeter_null(self):
        '''Invalid triangle perimeter handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for zero side lengths (0, 0, 4)."):
            triangle.perimeter(0, 0, 4)

    def test_perimeter_negative(self):
        '''Negative dimensions for triangle perimeter.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions (-2, 4, 6)."):
            triangle.perimeter(-2, 4, 6)
    
    def test_area_negative(self):
        '''Negative dimensions for triangle area.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimensions (-2, 8)."):
            triangle.area(-2, 8)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        '''Valid square area calculation.'''
        res = square.area(3)
        self.assertEqual(res, 9, msg=f"Expected area to be 9, but got {res}")
    
    def test_area_null(self):
        '''Invalid square area handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid dimension (0)."):
            square.area(0)
    
    def test_perimeter(self):
        '''Valid square perimeter calculation.'''
        res = square.perimeter(5)
        self.assertEqual(res, 20, msg=f"Expected perimeter to be 20, but got {res}")
    
    def test_perimeter_null(self):
        '''Invalid square perimeter handling.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid dimension (0)."):
            square.perimeter(0)

    def test_invalid_parametrs(self):
        '''Non-numeric square area inputs.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for non-numeric inputs ('a', 'b')."):
            square.area("a", "b")

    def test_invalid_parametrs_tuples(self):
        '''Tuple inputs for square area.'''
        with self.assertRaises(TypeError, msg="Expected TypeError for tuple inputs ((1, 2), (3, 4))."):
            square.area((1, 2), (3, 4))
    
    def test_perimeter_negative(self):
        '''Negative dimensions for square perimeter.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimension (-2)."):
            square.perimeter(-2)
    
    def test_area_negative(self):
        '''Negative dimensions for square area.'''
        with self.assertRaises(ValueError, msg="Expected ValueError for negative dimension (-2)."):
            square.area(-2)
