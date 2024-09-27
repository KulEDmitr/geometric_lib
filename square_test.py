from square import area, perimeter
import unittest


class SquareTestCase(unittest.TestCase):

    def test_0_area(self):
        area_result = area(0)
        self.assertEqual(area_result, 0)

    def test_1_area(self):
        area_result = area(10)
        self.assertEqual(area_result, 100)

    def test_2_area(self):
        area_result = area(123456789)
        self.assertEqual(area_result, 123456789 ** 2)



    def test_0_perimeter(self):
        perimeter_result = perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_1_perimeter(self):
        perimeter_result = perimeter(10)
        self.assertEqual(perimeter_result, 40)

    def test_2_perimeter(self):
        perimeter_result = perimeter(123456789)
        self.assertEqual(perimeter_result, 4 * 123456789)
