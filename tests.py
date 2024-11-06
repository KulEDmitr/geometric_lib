import unittest
import math

import square
import triangle
import rectangle
import circle

class TestGeometryFunctions(unittest.TestCase):

        '''square'''
        def test_square_area(self):
            self.assertEqual(square.area(4), 16)
            self.assertEqual(square.area(0), 0)
            self.assertAlmostEqual(square.area(2.5), 6.25)

        def test_square_perimeter(self):
            self.assertEqual(square.perimeter(4), 16)
            self.assertEqual(square.perimeter(0), 0)
            self.assertAlmostEqual(square.perimeter(2.5), 10)

        
        '''triangle'''
        def test_triangle_area(self):
            self.assertEqual(triangle.area(4 , 5 ), 10)
            self.assertEqual(triangle.area(0 , 4), 0)
            self.assertAlmostEqual(triangle.area(10 , 10), 50)

        def test_triangle_perimeter(self):
            self.assertEqual(triangle.perimeter(4 , 3 , 2), 9)
            self.assertEqual(triangle.perimeter(0 , 3 , 5), 0)
            self.assertAlmostEqual(triangle.perimeter(2.5 , 2.5 , 5), 10)
            
        '''rectangle'''    
        def test_rectangle_area(self):
            self.assertEqual(rectangle.area(3 ,3), 9)
            self.assertEqual(rectangle.area(10 , 10), 100)
            self.assertAlmostEqual(rectangle.area(2.5 , 2.5), 6.25)

        def test_rectangle_perimeter(self):
            self.assertEqual(rectangle.perimeter(4 , 5 ), 18)
            self.assertEqual(rectangle.perimeter(8 , 8), 32)
            self.assertAlmostEqual(rectangle.perimeter(10 , 10), 40)

        '''circle'''
        def test_rectangle_area(self):
            self.assertEqual(circle.area(3), math.pi * 3 * 3)
            self.assertEqual(circle.area(10), math.pi * 10 * 10)
            self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5 * 2.5)

        def test_rectangle_perimeter(self):
            self.assertEqual(circle.perimeter(4), 2 * math.pi * 4)
            self.assertEqual(circle.perimeter(0), 2 * math.pi * 0)
            self.assertAlmostEqual(circle.perimeter(10), 2 * math.pi * 10)