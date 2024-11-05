import unittest
import square

class SquareTestCase(unittest.TestCase):

    def test_1(self):
        assert square.area(0) == 0

    def test_2(self):
        assert square.area(10) == 100

    def test_3(self):
        assert square.area(8.5) == 72.25

    def test_4(self):
        assert square.perimeter(0) == 0

    def test_5(self):
        assert square.perimeter(10) == 40

    def test_6(self):
        assert square.perimeter(17.25) == 69

    def test_7(self):
        assert square.area(10) != 40

    def test_8(self):
        assert square.perimeter(10) != 30