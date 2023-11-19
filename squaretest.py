import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    #area_tests
    
    def test_square_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0, "Incorrect calculation area of square with side length 0")

    def test_square_natural_area(self):
        res = area(10)
        self.assertEqual(res, 100, " Incorrect calculation of the square area")

    def test_square_string_area(self):
        try:
            res = area('5')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_square_negative_area(self):
        try:
            res = area(-3)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_rectangle_extra_arguments_area(self):
        try:
            res = area(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_rectangle_missing_arguments_area(self):
        try:
            res = area()
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")

    #perimeter_tests
    
    def test_square_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0, "Incorrect calculation area of square with side length 0")

    def test_square_natural_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40, " Incorrect calculation of the square area")

    def test_square_string_perimeter(self):
        try:
            res = perimeter('123')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_square_negative_perimeter(self):
        try:
            res = perimeter(-7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_square_extra_arguments_perimeter(self):
        try:
            res = perimeter(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_square_missing_arguments_perimeter(self):
        try:
            res = perimeter()
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")
