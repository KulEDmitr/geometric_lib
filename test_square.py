import unittest
import square

class SquareAreaTest(unittest.TestCase):

    def test_area_basic(self, dec_place=4):
        tests_list = [\
            (12, 144),\
            (123.45, 15239.9025),\
            (0, 0)\
        ]
        for rad, exp in tests_list:
            self.assertAlmostEqual(square.area(rad), exp, dec_place)


    def test_area_invalid_value(self):
        tests_list = [-3, -0.1, -13, -56.78]
        for a in tests_list:
            self.assertRaises(ValueError, square.area, a)


    def test_area_invalid_type(self):
        tests_list = [("123"), ("aboba"), ([1]), ([2, 3])]
        for a in tests_list:
            self.assertRaises(TypeError, square.area, a)


class SquarePerimeterTest(unittest.TestCase):

    def test_perimeter_basic(self, dec_place=4):
        tests_list = [\
            (21, 84),\
            (321, 1284),\
            (0.1, 0.4),\
            (43.21, 172.84),\
            (0, 0)\
        ]
        for rad, exp in tests_list:
            self.assertAlmostEqual(square.perimeter(rad), exp, dec_place)


    def test_perimeter_invalid_value(self):
        tests_list = [(-3), (-0.1), (-63), (-78.45)]
        for a in tests_list:
            self.assertRaises(ValueError, square.perimeter, a)


    def test_perimeter_invalid_type(self):
        tests_list = [("123"), ("aboba"), ([1]), ([2, 3])]
        for a in tests_list:
            self.assertRaises(TypeError, square.perimeter, a)