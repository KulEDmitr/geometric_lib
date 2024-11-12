import unittest
from circle import area as circle_area
from circle import perimeter as circle_perimeter
from rectangle import area as rectangle_area
from rectangle import perimeter as rectangle_perimeter
from square import area as square_area
from square import perimeter as square_perimeter
from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter


class TestCaseCircle(unittest.TestCase):
    def test_area(self):
        res = circle_area(0)
        self.assertEqual(res, -1)
        res = circle_area('7')
        self.assertEqual(res, -1)
        res = circle_area(7)
        self.assertEqual(res, 153.93804002589985)


    def test_perimetr(self):
        res = circle_perimeter(0)
        self.assertEqual(res, -1)
        res = circle_perimeter('7')
        self.assertEqual(res, -1)
        res = circle_perimeter(7)
        self.assertEqual(res, 43.982297150257104)


class TestCaseRectangle(unittest.TestCase):
    def test_area(self):
        res = rectangle_area(0, 1)
        self.assertEqual(res, -1)
        res = rectangle_area(5, 6)
        self.assertEqual(res, 30)
        res = rectangle_area(5, '6')
        self.assertEqual(res, -1)

    def test_perimetr(self):
        res = rectangle_perimeter(0, 1)
        self.assertEqual(res, -1)
        res = rectangle_perimeter(5, '6')
        self.assertEqual(res, -1)
        res = rectangle_perimeter(5, 6)
        self.assertEqual(res, 22)


class TestCaseSquare(unittest.TestCase):
    def test_area(self):
        res = square_area(0)
        self.assertEqual(res, -1)
        res = square_area('5')
        self.assertEqual(res, -1)
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_perimetr(self):
        res = square_perimeter(0)
        self.assertEqual(res, -1)
        res = square_perimeter('5')
        self.assertEqual(res, -1)
        res = square_perimeter(5)
        self.assertEqual(res, 20)

class TestCaseTriangle(unittest.TestCase):
    def test_area(self):
        res = triangle_area(1, -1)
        self.assertEqual(res, -1)
        res = triangle_area(5, '6')
        self.assertEqual(res, -1)
        res = triangle_area(3, 2)
        self.assertEqual(res, 3)

    def test_perimetr(self):
        res = triangle_perimeter(5, 1, -1)
        self.assertEqual(res, -1)
        res = triangle_perimeter(5, '6', 1)
        self.assertEqual(res, -1)
        res = triangle_perimeter(5, 2, 1)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
