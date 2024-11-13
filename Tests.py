import unittest

import triangle, circle, rectangle, square


class TestGeometricLib(unittest.TestCase):

    ''' triangle tests'''
    
    def test_triangle_area_valid(self):
        self.assertEqual(triangle.area(5, 4), 10)
        self.assertEqual(triangle.area(3, 7), 10.5)  
        self.assertAlmostEqual(triangle.area(12.5, 6.4), 40, places = 4)
        self.assertAlmostEqual(triangle.area(2, 9.3), 9.3, places = 4)

    def test_triangle_area_str(self):
        with self.assertRaises(TypeError):
            triangle.area("1", "2")

    def test_triangle_area_zero(self):
        with self.assertRaises(ValueError):
            triangle.area(5, 0)

    def test_triangle_perimeter_valid(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(7, 24, 25), 56)
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.8, 4.1), 10.4, places = 4)
        self.assertAlmostEqual(triangle.perimeter(1.2, 3.6, 2.8), 7.6, places = 4)

    def test_triangle_perimeter_str(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", "2", "4")

    def test_triangle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 0, 6)

    def test_triangle_perimeter_notTriangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(2, 3, 7)


        
    ''' circle tests '''
    
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle.area(2), 12.5663706, places = 4)
        self.assertAlmostEqual(circle.area(2.5), 19.6349541, places = 4)

    def test_circle_area_str(self):
        with self.assertRaises(TypeError):
            circle.area("7")

    def test_circle_area_zero(self):
        with self.assertRaises(ValueError):
            circle.area(0)

    def test_circle_perimeter_valid(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.5663706, places = 4)
        self.assertAlmostEqual(circle.perimeter(2.5), 15.7079637, places = 4)

    def test_circle_perimeter_str(self):
        with self.assertRaises(TypeError):
            circle.perimeter("5")

    def test_circle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            circle.perimeter(0)



    ''' rectangle tests '''
    
    def test_rectangle_area_valid(self):
        self.assertEqual(rectangle.area(5, 4), 20)
        self.assertAlmostEqual(rectangle.area(5.6, 4.3), 24.08, places = 4)

    def test_rectangle_area_str(self):
        with self.assertRaises(TypeError):
            rectangle.area(4, "7")

    def test_rectangle_area_zero(self):
        with self.assertRaises(ValueError):
            rectangle.area(3, 0)

    def test_rectangle_perimeter_valid(self):
        self.assertEqual(rectangle.perimeter(5, 4), 18)
        self.assertAlmostEqual(rectangle.perimeter(5.6, 4.3), 19.8, places = 4)

    def test_rectangle_perimeter_str(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("5", 3)

    def test_rectangle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(0, 7)



    ''' square tests '''

    def test_square_area_valid(self):
        self.assertEqual(square.area(5), 25)
        self.assertAlmostEqual(square.area(7.7), 59.29, places = 4)

    def test_square_area_str(self):
        with self.assertRaises(TypeError):
            square.area("87")

    def test_square_area_zero(self):
        with self.assertRaises(ValueError):
            square.area(0)

    def test_square_perimeter_valid(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertAlmostEqual(square.perimeter(7.7), 30.8, places = 4)

    def test_square_perimeter_str(self):
        with self.assertRaises(TypeError):
            square.perimeter("9")

    def test_square_perimeter_zero(self):
        with self.assertRaises(ValueError):
            square.perimeter(0)


if __name__ == '__main__':
    unittest.main()
