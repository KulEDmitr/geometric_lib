import unittest
import triangle

class TriangleAreaTest(unittest.TestCase):

    def test_area_basic(self, dec_place=4):
        tests_list = [\
            (12, 34, 204),\
            (12, 2, 12),\
            (12, 2.5, 15),\
            (12.34, 5.5, 33.935)\
        ]
        for a, b, exp in tests_list:
            self.assertAlmostEqual(triangle.area(a, b), exp, dec_place)


    def test_area_invalid_value(self):
        tests_list = [(-3, 4), (-0.1, 5.7), (5, -13), (97, -56.78), (13, 0), (0, -56.78)]
        for a, b in tests_list:
            self.assertRaises(ValueError, triangle.area, a, b)
        

    def test_area_invalid_type(self):
        tests_list = [("123", 2), (545, "aboba"), ([1], 35), (78, [2, 3])]
        for a, b in tests_list:
            self.assertRaises(TypeError, triangle.area, a, b)


class TrianglePerimeterTest(unittest.TestCase):

    def test_perimeter_basic(self, dec_place=4):
        tests_list = [\
            (5, 6, 7, 18),\
            (5.1, 6, 7, 18.1),\
            (5, 6.2, 7, 18.2),\
            (5, 6, 7.3, 18.3)\
        ]
        for a, b, c, exp in tests_list:
            self.assertAlmostEqual(triangle.perimeter(a, b, c), exp, dec_place)


    def test_perimeter_invalid_value(self):
        tests_list = [\
            (-3, 4, 5), (3, -4, -5), (3, 4, -5),\
            (0, 4, 5), (3, 0, 5), (3, 4, 0),\
            (1, 2, 3), (100, 30, 40), (3453245, 4353, 3453)\
        ]
        for a, b, c in tests_list:
            self.assertRaises(ValueError, triangle.perimeter, a, b, c)


    def test_perimeter_invalid_type(self):
        tests_list = [\
            ("123", 45, 23), (86, "aboba", 231), (10, 43.4, "2fsd"),\
            ([1], 43, 98), (23, [2, 3], 52), (73, 12, [3])\
        ]
        for a, b, c in tests_list:
            self.assertRaises(TypeError, triangle.perimeter, a, b, c)