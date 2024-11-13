import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        assert circle.area(0) == 0

    def test_one_mul(self):
        assert circle.area(10) == 314.1592653589793

    def test_two_mul(self):
        assert circle.area(67.636) == 14371.619275936122

    def test_three_mul(self):
        assert circle.perimeter(0) == 0

    def test_four_mul(self):
        assert circle.perimeter(10) == 62.83185307179586

    def test_five_mul(self):
        assert circle.perimeter(67.636) == 424.96952143639845

    def test_six_mul(self):
        assert circle.area(10) != 40

    def test_seven_mul(self):
        assert circle.perimeter(10) != 30