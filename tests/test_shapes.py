import unittest
from unittest.mock import patch
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

# Вспомогательные функции для проверки на корректные значения
def validate_input(func):
    def wrapper(*args, **kwargs):
        # Проверка на неподходящие типы данных
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        # Проверка на отрицательные значения
        if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть неотрицательными")
        return func(*args, **kwargs)
    return wrapper

class TestRectangle(unittest.TestCase):
    @patch('rectangle.area', side_effect=validate_input(rect_area))
    def test_area(self, mock_area):
        # Проверка на корректные значения
        self.assertEqual(mock_area(10, 0), 0)
        self.assertEqual(mock_area(10, 10), 100)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_area(-10, 10)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_area("a", 10)
        with self.assertRaises(TypeError):
            mock_area([5, 10])
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_area(1e10, 1e10), 1e20)

    @patch('rectangle.perimeter', side_effect=validate_input(rect_perimeter))
    def test_perimeter(self, mock_perimeter):
        # Проверка на корректные значения
        self.assertEqual(mock_perimeter(10, 0), 20)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_perimeter(-10, 10)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_perimeter(10, "width")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_perimeter(1e10, 1e10), 4e10)

class TestSquare(unittest.TestCase):
    @patch('square.area', side_effect=validate_input(square_area))
    def test_area(self, mock_area):
        # Проверка на корректные значения
        self.assertEqual(mock_area(10), 100)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_area(-10)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_area("side")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_area(1e10), 1e20)

    @patch('square.perimeter', side_effect=validate_input(square_perimeter))
    def test_perimeter(self, mock_perimeter):
        # Проверка на корректные значения
        self.assertEqual(mock_perimeter(10), 40)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_perimeter(-10)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_perimeter("side")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_perimeter(1e10), 4e10)

class TestTriangle(unittest.TestCase):
    @patch('triangle.area', side_effect=validate_input(triangle_area))
    def test_area(self, mock_area):
        # Проверка на корректные значения
        self.assertEqual(mock_area(10, 5), 25)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_area(-10, 5)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_area("a", 5)
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_area(1e10, 1e10), 5e19)

    @patch('triangle.perimeter', side_effect=validate_input(triangle_perimeter))
    def test_perimeter(self, mock_perimeter):
        # Проверка на корректные значения
        self.assertEqual(mock_perimeter(3, 4, 5), 12)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_perimeter(3, -4, 5)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_perimeter(3, 4, "side")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_perimeter(1e10, 1e10, 1e10), 3e10)

class TestCircle(unittest.TestCase):
    @patch('circle.area', side_effect=validate_input(circle_area))
    def test_area(self, mock_area):
        # Проверка на корректные значения
        self.assertAlmostEqual(mock_area(7), 153.93804002589985)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_area(-7)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_area("radius")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_area(1e10), 3.141592653589793e20, delta=1e15)

    @patch('circle.perimeter', side_effect=validate_input(circle_perimeter))
    def test_perimeter(self, mock_perimeter):
        # Проверка на корректные значения
        self.assertAlmostEqual(mock_perimeter(7), 43.982297150257104)
        # Проверка на отрицательные значения
        with self.assertRaises(ValueError):
            mock_perimeter(-7)
        # Проверка на неправильные типы данных
        with self.assertRaises(TypeError):
            mock_perimeter("radius")
        # Проверка на очень большие значения
        self.assertAlmostEqual(mock_perimeter(1e10), 6.283185307179586e10)

if __name__ == '__main__':
    unittest.main()
