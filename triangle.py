import unittest

def area(a, h): 
    '''
    Возвращает площадь треугольника
        Входные данные:
        a (int) - длина основание треугольника
        h (int) - высота к основанию a
        
        Выходные данные:
        area (float) - площадь Треугольник
        
        Пример:
            area(5, 10) - вернёт 25
    '''
    if not isinstance(a, int) or not isinstance(h, int):
        raise TypeError("Сторона и высота треугольника должна быть целым числом")
    if a <= 0 or h <= 0:
        raise ValueError("Сторона и высота треугольника должна быть больше 0")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника
        Входные данные:
        a (int) - длина одной стороны треугольника
        b (int) - длина второй стороны треугольника
        c (int) - длина третьей стороны треугольника
        
        Выходные данные:
        perimeter (int) - периметр треугольника
        
        Пример:
            area(1, 2, 3) - вернёт 6
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError("Стороны треугольника должны быть целым числом")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть больше 0")
    return a + b + c 
    
class TriangleTests(unittest.TestCase):
    # Check area
    def test_area_pass_1(self):
        self.assertAlmostEqual(area(2, 4), 4, places=2)
    def test_area_pass_2(self):
        self.assertAlmostEqual(area(999221, 214531), 107181940175.5, places=2)
    
    def test_area_value_error_1(self):
        with self.assertRaises(ValueError):
            area(0, 1)
    def test_area_value_error_2(self):
        with self.assertRaises(ValueError):
            area(223, -3214234)
    
    def test_area_type_error_1(self):
        with self.assertRaises(TypeError):
            area('1', 23)
    def test_area_type_error_2(self):
        with self.assertRaises(TypeError):
            area(3324, "321")
    
    # Check perimeter
    def test_perimeter_pass_1(self):
        self.assertEqual(perimeter(4, 34, 23), 61)
    def test_perimeter_pass_2(self):
        self.assertEqual(perimeter(234, 23, 4325235), 4325492)
    
    def test_perimeter_value_error_1(self):
        with self.assertRaises(ValueError):
            perimeter(0, 324, 4)
    def test_perimeter_value_error_2(self):
        with self.assertRaises(ValueError):
            perimeter(432, 43, -4234234)
    
    def test_perimeter_type_error_1(self):
        with self.assertRaises(TypeError):
            perimeter(234, 4, '5')
    def test_perimeter_type_error_2(self):
        with self.assertRaises(TypeError):
            perimeter(65, "2343", 164)