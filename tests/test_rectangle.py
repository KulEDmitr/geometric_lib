import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):

    def test_area_normal_numbers(self):
        self.assertEqual(rectangle.area(23, 10.5), 241.5)
        self.assertEqual(rectangle.area(5, 5), 25)
        self.assertEqual(rectangle.area(1, 30), 30)
    
    def test_area_negative_numbers(self):
        self.assertRaises(Exception, rectangle.area, -1, 10)
        self.assertRaises(Exception, rectangle.area, 10, -2)
        self.assertRaises(Exception, rectangle.area, -2, -10)

    def test_area_strings(self):
        self.assertRaises(Exception, rectangle.area, "23", 2)
        self.assertRaises(Exception, rectangle.area, 2, "10")
        self.assertRaises(Exception, rectangle.area, "5", "10")
    
    def test_area_complex_oblects(self):
        self.assertRaises(Exception, rectangle.area, map, 2)

    def test_perimeter_normal_numbers(self):
        self.assertEqual(rectangle.perimeter(23, 10.5), 67.0)
        self.assertEqual(rectangle.perimeter(5, 5), 20)
        self.assertEqual(rectangle.perimeter(1, 30), 62)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, rectangle.perimeter, -1, 10)
        self.assertRaises(Exception, rectangle.perimeter, 10, -2)
        self.assertRaises(Exception, rectangle.perimeter, -2, -10)
    
    def test_perimeter_strings(self):
        self.assertRaises(Exception, rectangle.perimeter, "23", 2)
        self.assertRaises(Exception, rectangle.perimeter, 2, "10")
        self.assertRaises(Exception, rectangle.perimeter, "5", "10")
    
    def test_perimeter_complex_oblects(self):
        self.assertRaises(Exception, rectangle.perimeter, map, 1)
        self.assertRaises(Exception, rectangle.perimeter, 2, map)