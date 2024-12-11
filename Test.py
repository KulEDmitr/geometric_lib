import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle_lab import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(2), 12.56637061) #Тест с целым числом
        self.assertAlmostEqual(circle_area(1.5), 7.06858347) #Тест с дробным числом
        self.assertEqual(circle_area(0), 0) #Тест с нулевым радиусом
        with self.assertRaises(ValueError): #Тест с отрицательным радиусом
            circle_area(-1)
        
    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.84955592) #Тест с целым числом
        self.assertAlmostEqual(circle_perimeter(2.5), 15.70796326) #Тест с дробным числом
        self.assertEqual(circle_perimeter(0), 0) #Тест с нулевым радиусом
        with self.assertRaises(ValueError): #Тест с отрицательным радиусом
            circle_perimeter(-1)

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(2, 3), 6) #Тест с целыми числами
        self.assertAlmostEqual(rectangle_area(1.5, 2.5), 3.75) #Тест с дробными числами
        self.assertEqual(rectangle_area(0, 5), 0) #Тест с нулевой стороной
        with self.assertRaises(ValueError): #Тест с отрицательными сторонами
            rectangle_area(-1, 5)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10) #Тест с целыми числами
        self.assertAlmostEqual(rectangle_perimeter(1.5, 2.5), 8) #Тест с дробными числами
        self.assertEqual(rectangle_perimeter(0, 5), 10) #Тест с нулевой стороной
        with self.assertRaises(ValueError): #Тест с отрицательными сторонами
            rectangle_perimeter(-1, 5)

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(2), 4) #Тест с целым числом
        self.assertAlmostEqual(square_area(1.5), 2.25) #Тест с дробным числом
        self.assertEqual(square_area(0), 0) #Тест с нулевой стороной
        with self.assertRaises(ValueError): #Тест с отрицательной стороной
            square_area(-1)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(2), 8) #Тест с целым числом
        self.assertAlmostEqual(square_perimeter(1.5), 6) #Тест с дробным числом
        self.assertEqual(square_perimeter(0), 0) #Тест с нулевой стороной
        with self.assertRaises(ValueError): #Тест с отрицательной стороной
            square_perimeter(-1)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(3, 4), 12) #Тест с целыми числами
        self.assertAlmostEqual(triangle_area(2.5, 2), 5.0) #Тест с дробными числами
        with self.assertRaises(ValueError): #Тест с отрицательной стороной
            triangle_area(-1, 4)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12) #Тест с целыми числами
        self.assertAlmostEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5) #Тест с дробными числами
        with self.assertRaises(ValueError): #Тест с отрицательной стороной
            triangle_perimeter(-1, 4, 5)
        with self.assertRaises(ValueError): #Тест с невозможным треугольником
            triangle_perimeter(1, 1, 10)

if __name__ == '__main__':
    unittest.main()