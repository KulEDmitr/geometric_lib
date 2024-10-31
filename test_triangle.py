import unittest
import triangle

class TriangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert triangle.area(7,8) == 28

    def test_one_mul(self):
        assert triangle.area(10, 10) == 50


    def test_two_mul(self):
        assert triangle.area(7.5, 3.5) == 13.125


    def test_three_mul(self):
        assert triangle.perimeter(0, 0, 0) == 0


    def test_four_mul(self):
        assert triangle.perimeter(10, 6, 8) == 24


    def test_five_mul(self):
        assert triangle.perimeter(34.23, 42.34, 23.43) == 100

    def test_six_mul(self):
        assert triangle.area(10, 10) != 40

    def test_seven_mul(self):
        assert triangle.perimeter(10, 6, 8) != 30