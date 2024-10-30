import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

def validate_input(func):
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть неотрицательными")
        return func(*args, **kwargs)
    return wrapper

rect_area = validate_input(rect_area)
rect_perimeter = validate_input(rect_perimeter)
square_area = validate_input(square_area)
square_perimeter = validate_input(square_perimeter)
triangle_area = validate_input(triangle_area)
triangle_perimeter = validate_input(triangle_perimeter)
circle_area = validate_input(circle_area)
circle_perimeter = validate_input(circle_perimeter)

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rect_area(10, 0), 0)
        self.assertEqual(rect_area(10, 10), 100)
        self.assertAlmostEqual(rect_area(1e10, 1e10), 1e20)

    def test_perimeter(self):
        self.assertEqual(rect_perimeter(10, 0), 20)
        self.assertAlmostEqual(rect_perimeter(1e10, 1e10), 4e10)

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(10), 100)
        self.assertAlmostEqual(square_area(1e10), 1e20)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)
        self.assertAlmostEqual(square_perimeter(1e10), 4e10)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertAlmostEqual(triangle_area(1e10, 1e10), 5e19)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(triangle_perimeter(1e10, 1e10, 1e10), 3e10)

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(7), 153.93804002589985)
        self.assertAlmostEqual(circle_area(1e10), 3.141592653589793e20, delta=1e15)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(7), 43.982297150257104)
        self.assertAlmostEqual(circle_perimeter(1e10), 6.283185307179586e10)

if __name__ == '__main__':
    unittest.main()
