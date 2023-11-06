import unittest
import square

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