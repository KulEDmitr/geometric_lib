import unittest
from triangle import area, perimeter

class TriagleTestCase(unittest.TestCase):

    #area_tests
    
    def test_triangle_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0, "Incorrect calculation area of triangle with side length 0")

    def test_triangle_natural_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50, " Incorrect calculation of the triangle area")

    def test_triangle_string_area(self):
        try:
            res = area('5', '5')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_triangle_negative_area(self):
        try:
            res = area(-5, -7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_triangle_extra_arguments_area(self):
        try:
            res = area(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_triangle_missing_arguments_area(self):
        try:
            res = area(1)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")

    #perimeter_tests
    
    def test_triangle_zero_perimeter(self):
        res = perimeter(10, 0, 10)
        self.assertEqual(res, 0, "Incorrect calculation area of triangle with side length 0")

    def test_triangle_natural_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30, " Incorrect calculation of the triangle area")

    def test_triangle_string_perimeter(self):
        try:
            res = perimeter('123', '64', '123')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_triangle_negative_perimeter(self):
        try:
            res = perimeter(-13, -7, -2)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_triangle_extra_arguments_perimeter(self):
        try:
            res = perimeter(1, 23, 4, 2)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_triangle_missing_arguments_perimeter(self):
        try:
            res = perimeter(1)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")
