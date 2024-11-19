import unittest
import math

def circle_area(radius):
    if  radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * radius ** 2

def circle_perimeter(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r

def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return width * height

def rectangle_perimeter(width, height):
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (width + height)

def square_area(side):
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return side * side

def square_perimeter(side):
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return 4 * side

def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a + b + c

class TestShapesFunctions(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)

    

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.41592653589793)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-5)

    def test_circle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            circle_perimeter("string")

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_rectangle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "string")

    def test_square_area(self):
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square_area(-5)

    def test_square_area_invalid_type(self):
        with self.assertRaises(TypeError):
            square_area("string")

    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 10), 25)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            triangle_area(5, -10)

    def test_triangle_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle_perimeter(3, 4, "string")

if __name__ == '__main__':
    unittest.main()
