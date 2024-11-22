import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):

    def test_1(self):
        assert rectangle.area(0,13) == 0

    def test_2(self):
        assert rectangle.area(10,10) == 100

    def test_3(self):
        assert rectangle.area(65.5, 4.5) == 294.75

    def test_4(self):
        assert rectangle.perimeter(0,0) == 0

    def test_5(self):
        assert rectangle.perimeter(10, 54) == 128

    def test_6(self):
        assert rectangle.perimeter(67.636, 42.364) == 220

    def test_7(self):
        assert rectangle.area(7,8) != 70

    def test_8(self):
        assert rectangle.perimeter(10, 54) != 120