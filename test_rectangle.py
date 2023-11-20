import unittest
import rectangle

class RectangleAreaTest(unittest.TestCase):

    def test_area_basic(self, dec_place=4):
        tests_list = [\
            (12, 34, 408),\
            (1, 56, 56),\
            (5.4, 6.7, 36.18),\
            (12.34, 56, 691.04),\
            (0, 45, 0)\
        ]
        for a, b, exp in tests_list:
            self.assertAlmostEqual(rectangle.area(a, b), exp, dec_place)


    def test_area_invalid_value(self):
        tests_list = [(-3, 5), (-0.1, 8), (9, -13), (32, -56.78)]
        for a, b in tests_list:
            self.assertRaises(ValueError, rectangle.area, a, b)


    def test_area_invalid_type(self):
        tests_list = [(45, "123"), ("aboba", 87), ([1], 236), (543, [2, 3])]
        for a, b in tests_list:
            self.assertRaises(TypeError, rectangle.area, a, b)


class RectanglePerimeterTest(unittest.TestCase):

    def test_perimeter_basic(self, dec_place=4):
        tests_list = [\
            (21, 54, 150),\
            (321, 56.7, 755.4),\
            (12.7, 76.2, 177.8),\
            (43.21, 0, 86.42),\
            (0, 0, 0)\
        ]
        for a, b, exp in tests_list:
            self.assertAlmostEqual(rectangle.perimeter(a, b), exp, dec_place)


    def test_perimeter_invalid_value(self):
        tests_list = [(-3, 5), (-0.1, 8), (9, -13), (32, -56.78)]
        for a, b in tests_list:
            self.assertRaises(ValueError, rectangle.perimeter, a, b)


    def test_perimeter_invalid_type(self):
        tests_list = [(45, "123"), ("aboba", 87), ([1], 236), (543, [2, 3])]
        for a, b in tests_list:
            self.assertRaises(TypeError, rectangle.perimeter, a, b)
