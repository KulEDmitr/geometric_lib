import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_yes(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_circle_area_no(self):
        res = area(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_area_real_numbers(self):
        res = area(4.25)
        self.assertEqual(res, 56.745017305465645)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_yes(self):
        res = perimeter(4)
        self.assertEqual(res, 25.132741228718345)

    def test_circle_perimeter_no(self):
        res = perimeter(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_perimeter_real_numbers(self):
        res = perimeter(4.25)
        self.assertEqual(res, 26.703537555513243)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()