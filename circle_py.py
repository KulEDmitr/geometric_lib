from circle import area, perimeter
from math import pi

import unittest


class CircleTestCase(unittest.TestCase):

    def test_0_area(self):
        area_result = area(0)
        self.assertEqual(area_result, 0)

    def test_1_area(self):
        area_result = area(123)
        self.assertEqual(area_result, pi * (123 ** 2))

    @unittest.expectedFailure
    def test_2_area(self):
        area_result = area("abcd")
        self.assertEqual(area_result, TypeError)

    def test_3_area(self):
        area_result = area(-99)
        self.assertEqual(area_result, TypeError)



    def test_0_perimeter(self):
        perimeter_result = perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_1_perimeter(self):
        perimeter_result = perimeter(123)
        self.assertEqual(perimeter_result, 2 * pi * 123)

    @unittest.expectedFailure
    def test_2_perimeter(self):
        perimeter_result = perimeter("abcd")
        self.assertEqual(perimeter_result, TypeError)

    def test_3_perimeter(self):
        perimeter_result = perimeter(-99)
        self.assertEqual(perimeter_result, TypeError)

