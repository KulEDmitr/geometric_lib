import unittest
import actions
import circle
import rectangle
import square
import triangle


class ActionsTestCase(unittest.TestCase):
    def testZeroSum(self):
       res = actions.F_sum(0, 0)
       self.assertEqual(res, 0)
       
    def testSmallSum(self):
       res = actions.F_sum(13, 15)
       self.assertEqual(res, 28)
    
    def testBigSum(self):
       res = actions.F_sum(12345678, 76543210)
       self.assertEqual(res, 88888888)

    def testZeroMult(self):
       res = actions.F_mult(10, 0)
       self.assertEqual(res, 0)

    def testSmallMult(self):
       res = actions.F_mult(13, 15)
       self.assertEqual(res, 195)

    def testBigMult(self):
       res = actions.F_mult(12345678, 76543210)
       self.assertEqual(res, 944977823746380)


class CircleTestCase(unittest.TestCase):
    def testZeroArea(self):
       res = circle.area(0)
       self.assertEqual(res, 0)
       
    def testSmallArea(self):
       res = circle.area(13)
       self.assertEqual(round(res, 5), 530.92916)
    
    def testBigArea(self):
       res = circle.area(12345678)
       self.assertEqual(round(res, 5), 478828248493921.5)

    def testZeroPerimeter(self):
       res = circle.perimeter(0)
       self.assertEqual(res, 0)

    def testSmallPerimeter(self):
       res = circle.perimeter(13)
       self.assertEqual(round(res, 5), 81.68141)

    def testBigPerimeter(self):
       res = circle.perimeter(12345678)
       self.assertEqual(round(res, 5), 77570182.61677)


class RectangleTestCase(unittest.TestCase):
    def testZeroArea(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def testSmallArea(self):
       res = rectangle.area(13, 15)
       self.assertEqual(res, 195)
    
    def testBigArea(self):
       res = rectangle.area(12345678, 76543210)
       self.assertEqual(res, 944977823746380)

    def testZeroPerimeter(self):
       res = rectangle.perimeter(0, 0)
       self.assertEqual(res, 0)

    def testSmallPerimeter(self):
       res = rectangle.perimeter(13, 15)
       self.assertEqual(res, 56)

    def testBigPerimeter(self):
       res = rectangle.perimeter(12345678, 76543210)
       self.assertEqual(res, 177777776)


class SquareTestCase(unittest.TestCase):
    def testZeroArea(self):
       res = square.area(0)
       self.assertEqual(res, 0)
       
    def testSmallArea(self):
       res = square.area(13)
       self.assertEqual(res, 169)
    
    def testBigArea(self):
       res = square.area(12345678)
       self.assertEqual(res, 152415765279684)

    def testZeroPerimeter(self):
       res = square.perimeter(0)
       self.assertEqual(res, 0)

    def testSmallPerimeter(self):
       res = square.perimeter(13)
       self.assertEqual(res, 52)

    def testBigPerimeter(self):
       res = square.perimeter(12345678)
       self.assertEqual(res, 49382712)


class TriangleTestCase(unittest.TestCase):
    def testZeroArea(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def testSmallArea(self):
       res = triangle.area(13, 15)
       self.assertEqual(res, 97.5)
    
    def testBigArea(self):
       res = triangle.area(12345678, 76543210)
       self.assertEqual(res, 472488911873190)

    def testZeroPerimeter(self):
       res = triangle.perimeter(0, 0, 0)
       self.assertEqual(res, 0)

    def testSmallPerimeter(self):
       res = triangle.perimeter(13, 15, 17)
       self.assertEqual(res, 45)

    def testBigPerimeter(self):
       res = triangle.perimeter(12345678, 76543210, 23456789)
       self.assertEqual(res, 112345677)