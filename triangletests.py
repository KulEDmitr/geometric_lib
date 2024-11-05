import unittest
import triangle

class TriangleTestCase(unittest.TestCase):

    def test_1(self):
        assert triangle.area(7,8) == 28

    def test_2(self):
        assert triangle.area(10, 10) == 50


    def test_3(self):
        assert triangle.area(7.5, 3.5) == 13.125


    def test_4(self):
        assert triangle.perimeter(0, 0, 0) == 0


    def test_5(self):
        assert triangle.perimeter(10, 6, 8) == 24


    def test_6(self):
        assert triangle.perimeter(34.23, 42.34, 23.43) == 100

    def test_7(self):
        assert triangle.area(10, 10) != 40

    def test_8(self):
        assert triangle.perimeter(10, 6, 8) != 30