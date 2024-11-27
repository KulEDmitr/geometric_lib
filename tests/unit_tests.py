import unittest
from rectangle import area as rect_compute_area, perimeter as rect_compute_perimeter
from square import area_square as square_calculate_area, perimeter_square as square_calculate_perimeter
from triangle import area as triangle_find_area, perimeter as triangle_find_perimeter
from circle import area_circle as circle_determine_area, perimeter_circle as circle_determine_perimeter

def check_arguments(func):
    def inner(*args, **kwargs):
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Все аргументы должны быть числами")
        if any(arg <= 0 for arg in args):
            raise ValueError("Все аргументы должны быть положительными числами")
        return func(*args, **kwargs)
    return inner

# Оборачиваем функции для проверки аргументов
rect_compute_area = check_arguments(rect_compute_area)
rect_compute_perimeter = check_arguments(rect_compute_perimeter)
square_calculate_area = check_arguments(square_calculate_area)
square_calculate_perimeter = check_arguments(square_calculate_perimeter)
triangle_find_area = check_arguments(triangle_find_area)
triangle_find_perimeter = check_arguments(triangle_find_perimeter)
circle_determine_area = check_arguments(circle_determine_area)
circle_determine_perimeter = check_arguments(circle_determine_perimeter)

# Тесты для прямоугольника
class RectangleTests(unittest.TestCase):
    def test_area_valid_cases(self):
        self.assertEqual(rect_compute_area(15, 4), 60)
        self.assertAlmostEqual(rect_compute_area(1e8, 2e7), 2e15)

    def test_area_invalid_cases(self):
        with self.assertRaises(ValueError):
            rect_compute_area(-1, 5)
        with self.assertRaises(TypeError):
            rect_compute_area("15", 4)

    def test_perimeter_valid_cases(self):
        self.assertEqual(rect_compute_perimeter(15, 4), 38)
        self.assertAlmostEqual(rect_compute_perimeter(1e8, 2e7), 2.4e8)

    def test_perimeter_invalid_cases(self):
        with self.assertRaises(ValueError):
            rect_compute_perimeter(-15, 4)
        with self.assertRaises(TypeError):
            rect_compute_perimeter([15], 4)

# Тесты для квадрата
class SquareTests(unittest.TestCase):
    def test_area_valid_cases(self):
        self.assertEqual(square_calculate_area(6), 36)
        self.assertAlmostEqual(square_calculate_area(3e4), 9e8)

    def test_area_invalid_cases(self):
        with self.assertRaises(ValueError):
            square_calculate_area(-6)
        with self.assertRaises(TypeError):
            square_calculate_area(None)

    def test_perimeter_valid_cases(self):
        self.assertEqual(square_calculate_perimeter(6), 24)
        self.assertAlmostEqual(square_calculate_perimeter(5e4), 2e5)

    def test_perimeter_invalid_cases(self):
        with self.assertRaises(ValueError):
            square_calculate_perimeter(-8)
        with self.assertRaises(TypeError):
            square_calculate_perimeter("6")

# Тесты для треугольника
class TriangleTests(unittest.TestCase):
    def test_area_valid_cases(self):
        self.assertEqual(triangle_find_area(10, 8), 40)
        self.assertAlmostEqual(triangle_find_area(3e6, 4e6), 6e12)

    def test_area_invalid_cases(self):
        with self.assertRaises(ValueError):
            triangle_find_area(-10, 8)
        with self.assertRaises(TypeError):
            triangle_find_area("10", 8)

    def test_perimeter_valid_cases(self):
        self.assertEqual(triangle_find_perimeter(7, 24, 25), 56)
        self.assertAlmostEqual(triangle_find_perimeter(1e7, 1e7, 1e7), 3e7)

    def test_perimeter_invalid_cases(self):
        with self.assertRaises(ValueError):
            triangle_find_perimeter(10, -20, 15)
        with self.assertRaises(TypeError):
            triangle_find_perimeter("7", 24, 25)

# Тесты для круга
class CircleTests(unittest.TestCase):
    def test_area_valid_cases(self):
        self.assertAlmostEqual(circle_determine_area(9), 254.46900494077323, places=5)
        self.assertAlmostEqual(circle_determine_area(1e5), 3.141592653589793e10, delta=1e4)

    def test_area_invalid_cases(self):
        with self.assertRaises(ValueError):
            circle_determine_area(0)
        with self.assertRaises(TypeError):
            circle_determine_area({"radius": 7})

    def test_perimeter_valid_cases(self):
        self.assertAlmostEqual(circle_determine_perimeter(9), 56.548667764616276, places=5)
        self.assertAlmostEqual(circle_determine_perimeter(1e5), 628318.5307179586)

    def test_perimeter_invalid_cases(self):
        with self.assertRaises(ValueError):
            circle_determine_perimeter(-9)
        with self.assertRaises(TypeError):
            circle_determine_perimeter([9])

if __name__ == '__main__':
    unittest.main()
