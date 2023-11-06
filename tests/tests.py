import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):

    def test_area_normal_numbers(self):
        self.assertAlmostEqual(circle.area(2), 12.57, places=2)
        self.assertAlmostEqual(circle.area(10.5), 346.36, places=2)
        self.assertAlmostEqual(circle.area(0.5), 0.79, places=2)
    
    def test_area_negative_numbers(self):
        self.assertRaises(Exception, circle.area, -1)
        self.assertRaises(Exception, circle.area, -10)
        self.assertRaises(Exception, circle.area, -2)

    def test_area_strings(self):
        self.assertRaises(Exception, circle.area, "23")
        self.assertRaises(Exception, circle.area, "10")
        self.assertRaises(Exception, circle.area, "5")
    
    def test_area_complex_oblects(self):
        self.assertRaises(Exception, circle.area, map)

    def test_perimeter_normal_numbers(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.57, places=2)
        self.assertAlmostEqual(circle.perimeter(10.5), 65.97, places=2)
        self.assertAlmostEqual(circle.perimeter(0), 0.0, places=2)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, circle.perimeter, -1)
        self.assertRaises(Exception, circle.perimeter, -10)
        self.assertRaises(Exception, circle.perimeter, -2)
    
    def test_perimeter_strings(self):
        self.assertRaises(Exception, circle.perimeter, "23")
        self.assertRaises(Exception, circle.perimeter, "10")
        self.assertRaises(Exception, circle.perimeter, "5")
    
    def test_perimeter_complex_oblects(self):
        self.assertRaises(Exception, circle.perimeter, map)

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

class SquareTestCase(unittest.TestCase):

    def test_area_normal_numbers(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(2.5), 6.25)
        self.assertEqual(square.area(0), 0)
    
    def test_area_negative_numbers(self):
        self.assertRaises(Exception, square.area, -1)
        self.assertRaises(Exception, square.area, -10)
        self.assertRaises(Exception, square.area, -2)

    def test_area_strings(self):
        self.assertRaises(Exception, square.area, "23")
        self.assertRaises(Exception, square.area, "10")
        self.assertRaises(Exception, square.area, "5")
    
    def test_area_complex_oblects(self):
        self.assertRaises(Exception, square.area, map)

    def test_perimeter_normal_numbers(self):
        self.assertEqual(square.perimeter(4), 16)
        self.assertEqual(square.perimeter(2.5), 10.0)
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, square.perimeter, -1)
        self.assertRaises(Exception, square.perimeter, -10)
        self.assertRaises(Exception, square.perimeter, -2)
    
    def test_perimeter_strings(self):
        self.assertRaises(Exception, square.perimeter, "23")
        self.assertRaises(Exception, square.perimeter, "10")
        self.assertRaises(Exception, square.perimeter, "5")
    
    def test_perimeter_complex_oblects(self):
        self.assertRaises(Exception, square.perimeter, map)

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
