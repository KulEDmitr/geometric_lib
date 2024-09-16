import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    #area_tests
    
    def test_rectangle_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0, "Incorrect calculation area of rectangle with side length 0")

    def test_rectangle_natural_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100, " Incorrect calculation of the rectangle area")

    def test_rectangle_string_area(self):
        try:
            res = area('5', '5')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_rectangle_negative_area(self):
        try:
            res = area(-123, -7)
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
            res = area(1)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")

    #perimeter_tests
    
    def test_rectangle_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 0, "Incorrect calculation area of rectangle with side length 0")

    def test_rectangle_natural_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40, " Incorrect calculation of the rectangle area")

    def test_rectangle_string_perimeter(self):
        try:
            res = perimeter('123', '52')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_rectangle_negative_perimeter(self):
        try:
            res = perimeter(-13, -7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_rectangle_extra_arguments_perimeter(self):
        try:
            res = perimeter(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_rectangle_missing_arguments_perimeter(self):
        try:
            res = perimeter(1)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")
