import unittest
from rectangle import Rectangle
from circle import Circle
from square import Square
from triangle import Triangle

class RectangleTestCase(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle.area("15")
            Rectangle.perimeter("15")
    
    def test_area_zero(self):
        res = Rectangle.area(10, 0)
        self.assertEqual(res, 0)
        
    def test_perimeter_zero(self):
        res = Rectangle.perimeter(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_integers(self):
        res = Rectangle.area(13, 87)
        self.assertEqual(res, 1131)
    
    def test_perimeter_integers(self):
        res = Rectangle.perimeter(13, 87)
        self.assertEqual(res, 1131)
        
    def test_area_double(self):
        res = Rectangle.area(5.6, 7.8)
        self.assertEqual(res, 43.68)
        
    def test_perimeter_double(self):
        res = Rectangle.perimeter(5.6, 7.8)
        self.assertEqual(res, 43.68)
        
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            Rectangle.area(-27, 44)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            Rectangle.perimeter(-27, 44)

class CircleTestCase(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            Circle.area("15")
            Circle.perimeter("15")
            
    def test_zero(self):
        res = Circle.area(0)
        self.assertEqual(res, 0)
        res = Circle.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_area_integer(self):
        res = Circle.area(15)
        self.assertEqual(res, 706.8583470577034)
    
    def test_area_double(self):
        res = Circle.area(33.3)
        self.assertEqual(res, 3483.6806776391854)
        
    def test_perimeter_double(self):
        res = Circle.perimeter(52.3)
        self.assertEqual(res, 328.6105915654923)
        
    def test_perimeter_integer(self):
        res = Circle.perimeter(173)
        self.assertEqual(res, 1086.9910581420684)
        
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            Circle.area(-27)
            
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            Circle.perimeter(-78)

class SquareTestCase(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            Square.area("15")
            Square.perimeter("15")
            
    def test_zero(self):
        res = Square.area(0)
        self.assertEqual(res, 0)
        res = Square.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_area_integer(self):
        res = Square.area(15)
        self.assertEqual(res, 225)
    
    def test_area_double(self):
        res = Square.area(33.3)
        self.assertEqual(res, 1108.8899999999999)
        
    def test_perimeter_double(self):
        res = Square.perimeter(52.3)
        self.assertEqual(res, 209.2)
        
    def test_perimeter_integer(self):
        res = Square.perimeter(173)
        self.assertEqual(res, 692)
        
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            Square.area(-27)
            
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            Square.perimeter(-78)

class TriangleTestCase(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            Triangle.area("15")
            Triangle.perimeter("15")
            
    def test_zero(self):
        res = Triangle.area(0, 0)
        self.assertEqual(res, 0)
        res = Triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        
    def test_area_integer(self):
        res = Triangle.area(15, 6)
        self.assertEqual(res, 45)
    
    def test_area_double(self):
        res = Triangle.area(33.3, 44.4)
        self.assertEqual(res, 739.2599999999999)
        
    def test_perimeter_double(self):
        res = Triangle.perimeter(52.3, 26.7, 98)
        self.assertEqual(res, 177)
        
    def test_perimeter_integer(self):
        res = Triangle.perimeter(173, 478, 129)
        self.assertEqual(res, 780)
        
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            Triangle.area(-27, 24)
            
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            Triangle.perimeter(-78, 95, -15)

