import unittest
import circle, rectangle, square, triangle


class CircleTestCase(unittest.TestCase):
   def test_circle_area_res(self):
       res = circle.area(10)
       self.assertEqual(res, 314)
       
   def test_circle_area_minus(self):
       res = circle.area(-5)
       self.assertEqual(res, "Incorrect input")

   def test_circle_perimetr_res(self):
       res = circle.perimetr(100)
       self.assertEqual(res, 628)
       
   def test_circle_perimetr_str(self):
       res = circle.perimetr("арбуз")
       self.assertEqual(res, "Incorrect input") 

class RectangleTestCase(unittest.TestCase):

   def test_rectangle_area_res(self):
       res = rectangle.area(5, 2)
       self.assertEqual(res, 10)

   def test_rectangle_area_str(self):
        res = rectangle.area("lol", 8)
        self.assertEqual(res, "Incorrect input") 

   def test_rectangle_perimetr_res(self):
       res = rectangle.perimetr(5, 2)
       self.assertEqual(res, 14)

   def test_rectangle_perimetr_minus(self):
       res = rectangle.perimetr(-3, 5)
       self.assertEqual(res, "Incorrect input")
       
class SquareTestCase(unittest.TestCase):
   def test_square_area_res(self):
       res = square.area(3)
       self.assertEqual(res, 9)
       
   def test_square_area_minus(self):
       res = square.area(-7)
       self.assertEqual(res, "Incorrect input")

   def test_square_perimetr_res(self):
       res = square.perimetr(3)
       self.assertEqual(res, 12)
       
   def test_square_perimetr_str(self):
       res = square.perimetr("vibe")
       self.assertEqual(res, "Incorrect input")    

class TriangleTestCase(unittest.TestCase):
   def test_triangle_area_res(self):
       res = triangle.area(3, 6)
       self.assertEqual(res, 9)

   def test_triangle_area_str(self):
       res = triangle.area("a", "b")
       self.assertEqual(res, "Incorrect input")  
    
   def test_triangle_perimetr_res(self):
       res = triangle.perimetr(2, 7, 3)
       self.assertEqual(res, 12)

   def test_triangle_perimetr_minus(self):
       res = triangle.perimetr(-4, -1, -6)
       self.assertEqual(res, "Incorrect input")




   