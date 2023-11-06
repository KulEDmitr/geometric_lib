import unittest
import circle

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
