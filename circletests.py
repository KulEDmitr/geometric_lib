import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_1(self):
        assert circle.area(0) == 0

    def test_2(self):
        assert circle.area(10) == 314.1592653589793

    def test_3(self):
        assert circle.area(67.636) == 14371.619275936122

    def test_4(self):
        assert circle.perimeter(0) == 0

    def test_5(self):
        assert circle.perimeter(10) == 62.83185307179586

    def test_6(self):
        assert circle.perimeter(67.636) == 424.96952143639845

    def test_7(self):
        assert circle.area(10) != 40

    def test_8(self):
        assert circle.perimeter(10) != 30