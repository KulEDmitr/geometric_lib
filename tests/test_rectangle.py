import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert rectangle.area(0,13) == 0

    def test_one_mul(self):
        assert rectangle.area(10,10) == 100

    def test_two_mul(self):
        assert rectangle.area(65.5, 4.5) == 294.75


    def test_three_mul(self):
        assert rectangle.perimeter(0,0) == 0


    def test_four_mul(self):
        assert rectangle.perimeter(10, 54) == 128

    def test_five_mul(self):
        assert rectangle.perimeter(67.636, 42.364) == 220

    def test_six_mul(self):
        assert rectangle.area(7,8) != 70

    def test_seven_mul(self):
        assert rectangle.perimeter(10, 54) != 120