import unittest
import math
import circle


class CircleAreaTest(unittest.TestCase):

    def test_area_basic(self, dec_place=4):
        tests_list = [\
            (12, math.pi * 12 * 12),\
            (123, math.pi * 123 * 123),\
            (1/math.pi, 1/math.pi),\
            (12.34, math.pi * 12.34 * 12.34),\
            (0, 0)\
        ]
        for rad, exp in tests_list:
            self.assertAlmostEqual(circle.area(rad), exp, dec_place)


    def test_area_invalid_value(self):
        tests_list = [-3, -0.1, -13, -56.78]
        for rad in tests_list:
            self.assertRaises(ValueError, circle.area, rad)


    def test_area_invalid_type(self):
        tests_list = [("123"), ("aboba"), ([1]), ([2, 3])]
        for rad in tests_list:
            self.assertRaises(TypeError, circle.area, rad)


class CirclePerimeterTest(unittest.TestCase):

    def test_perimeter_basic(self, dec_place=4):
        tests_list = [\
            (21, 2 * math.pi * 21),\
            (321, 2 * math.pi * 321),\
            (1/math.pi, 2),\
            (43.21, 2 * math.pi * 43.21),\
            (0, 0)\
        ]
        for rad, exp in tests_list:
            self.assertAlmostEqual(circle.perimeter(rad), exp, dec_place)


    def test_perimeter_invalid_value(self):
        tests_list = [(-3), (-0.1), (-63), (-78.45)]
        for rad in tests_list:
            self.assertRaises(ValueError, circle.perimeter, rad)


    def test_perimeter_invalid_type(self):
        tests_list = [("123"), ("aboba"), ([1]), ([2, 3])]
        for rad in tests_list:
            self.assertRaises(TypeError, circle.perimeter, rad)
        