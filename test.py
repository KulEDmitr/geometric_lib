import unittest

from rectangle import area as rectangle_area
from rectangle import perimeter as rectangle_perimeter


from square import area as square_area
from square import perimeter as square_perimeter

from circle import area as circle_area
from circle import perimeter as circle_perimeter

from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = rectangle_area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = rectangle_area(10, 10)
       self.assertEqual(res, 100)
       
    def test_rectangle_mul(self):
       res = rectangle_area(4, 5)
       self.assertEqual(res, 20)
       
    def test_zero_plus(self):
       res = rectangle_perimeter(10, 0)
       self.assertEqual(res, 20)
       
    def test_square_plus(self):
       res = rectangle_perimeter(10, 10)
       self.assertEqual(res, 40)
       
    def test_rectangle_plus(self):
       res = rectangle_perimeter(3, 6)
       self.assertEqual(res, 18)



class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = square_area(0)
       self.assertEqual(res, 0)
       
    def test_ten_mul(self):
       res = square_area(10)
       self.assertEqual(res, 100)
       
    def test_four_mul(self):
       res = square_area(4)
       self.assertEqual(res, 16)
       
    def test_zero_plus(self):
       res = square_perimeter(0)
       self.assertEqual(res, 0)
       
    def test_ten_plus(self):
       res = square_perimeter(10)
       self.assertEqual(res, 40)
       
    def test_four_plus(self):
       res = square_perimeter(4)
       self.assertEqual(res, 16)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = circle_area(0)
       self.assertEqual(res, 0)
       
    def test_ten_mul(self):
       res = circle_area(10)
       self.assertEqual(res, 314.1592653589793)
       
    def test_four_mul(self):
       res = circle_area(4)
       self.assertEqual(res, 50.26548245743669)
       
    def test_zero_plus(self):
       res = circle_perimeter(0)
       self.assertEqual(res, 0)
       
    def test_ten_plus(self):
       res = circle_perimeter(10)
       self.assertEqual(res, 62.83185307179586)
       
    def test_four_plus(self):
       res = circle_perimeter(4)
       self.assertEqual(res, 25.132741228718345)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = triangle_area(0,10)
       self.assertEqual(res, 0)
       
    def test_ten_mul(self):
       res = triangle_area(10,10)
       self.assertEqual(res, 50)
       
    def test_four_mul(self):
       res = triangle_area(3,7)
       self.assertEqual(res, 10.5)
       
    def test_zero_plus(self):
       res = triangle_perimeter(0,0,0)
       self.assertEqual(res, 0)
       
    def test_ten_plus(self):
       res = triangle_perimeter(10,10,10)
       self.assertEqual(res, 30)
       
    def test_four_plus(self):
       res = triangle_perimeter(4,3,4)
       self.assertEqual(res, 11)


