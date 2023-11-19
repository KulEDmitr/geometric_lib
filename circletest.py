import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    #area_tests
    
    def test_circle_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0, "Incorrect calculation area of circle with side length 0")

    def test_circle_natural_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi , " Incorrect calculation of the circle area")

    def test_circle_string_area(self):
        try:
            res = area('5')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_circle_negative_area(self):
        try:
            res = area(-7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_circle_extra_arguments_area(self):
        try:
            res = area(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_circle_missing_arguments_area(self):
        try:
            res = area()
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")

    #perimeter_tests
    
    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0, "Incorrect calculation area of circle with side length 0")

    def test_circle_natural_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi, " Incorrect calculation of the circle area")

    def test_circle_string_perimeter(self):
        try:
            res = perimeter("52")
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for string type of arguments")

    def test_circle_negative_perimeter(self):
        try:
            res = perimeter(-52)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, ValueError, "Incorrect exception for negative arguments")

    def test_circle_extra_arguments_perimeter(self):
        try:
            res = perimeter(1, 23, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for excessive number of arguments")

    def test_circle_missing_arguments_perimeter(self):
        try:
            res = perimeter()
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect exception for insufficient number of arguments")

