import unittest
import square

class SquareTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert square.area(0) == 0

    def test_one_mul(self):
        assert square.area(10) == 100

    def test_two_mul(self):
        assert square.area(8.5) == 72.25

    def test_three_mul(self):
        assert square.perimeter(0) == 0

    def test_four_mul(self):
        assert square.perimeter(10) == 40

    def test_five_mul(self):
        assert square.perimeter(17.25) == 69

    def test_six_mul(self):
        assert square.area(10) != 40

    def test_seven_mul(self):
        assert square.perimeter(10) != 30