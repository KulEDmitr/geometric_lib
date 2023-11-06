import unittest
import triangle 

class TriangleTestCase(unittest.TestCase):

    def test_area_normal_numbers(self):
        self.assertEqual(triangle.area(3, 1.5), 2.25)
        self.assertEqual(triangle.area(5, 5), 12.5)
        self.assertEqual(triangle.area(2, 10), 10)
    
    def test_area_negative_numbers(self):
        self.assertRaises(Exception, triangle.area, -1, 10)
        self.assertRaises(Exception, triangle.area, 2, -10)
        self.assertRaises(Exception, triangle.area, -2, -3)

    def test_area_strings(self):
        self.assertRaises(Exception, triangle.area, "23", 2)
        self.assertRaises(Exception, triangle.area, 2, "10")
        self.assertRaises(Exception, triangle.area, "5", "10")
    
    def test_area_complex_oblects(self):
        self.assertRaises(Exception, triangle.area, map, 2)

    def test_perimeter_normal_numbers(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(10, 10, 2.5), 22.5)
        self.assertEqual(triangle.perimeter(23, 10, 15), 48)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, triangle.perimeter, -1, 2, 3)
        self.assertRaises(Exception, triangle.perimeter, -15, -10, 3)
        self.assertRaises(Exception, triangle.perimeter, -2, -20, -2)
    
    def test_perimeter_strings(self):
        self.assertRaises(Exception, triangle.perimeter, "23", 12, "12")
        self.assertRaises(Exception, triangle.perimeter, 10, 12, "10")
        self.assertRaises(Exception, triangle.perimeter, "5", "2", "10")
    
    def test_perimeter_complex_oblects(self):
        self.assertRaises(Exception, triangle.perimeter, map, 2, 2)        
