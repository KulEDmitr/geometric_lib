import unittest

def area(a, b): 
    '''
    Возвращает площадь прямоугольника
        Входные данные:
        a (int) - длина прямоугольника
        b (int) - ширина прямоугольника
        
        Выходные данные:
        area (int) - площадь прямоугольника
        
        Пример:
            area(5, 10) - вернёт 50
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Стороны прямоугольника должны быть целым числом")
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть больше 0")
    return a * b 

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника
        Входные данные:
        a (int) - длина прямоугольника
        b (int) - ширина прямоугольника
        
        Выходные данные:
        perimeter (int) - периметр прямоугольника
        
        Пример:
            perimeter(5, 10) - вернёт 30
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Стороны прямоугольника должны быть целым числом")
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть больше 0")
    return 2 * (a + b)

class RectangleTests(unittest.TestCase):
    # Check area
    def test_area_pass_1(self):
        self.assertEqual(area(2, 4), 8)
    def test_area_pass_2(self):
        self.assertEqual(area(999221, 214531), 214363880351)
    
    def test_area_value_error_1(self):
        with self.assertRaises(ValueError):
            area(0, 134)
    def test_area_value_error_2(self):
        with self.assertRaises(ValueError):
            area(61, -634764)
    
    def test_area_type_error_1(self):
        with self.assertRaises(TypeError):
            area('4', 8395142)
    def test_area_type_error_2(self):
        with self.assertRaises(TypeError):
            area(897653, "982662945645")
    
    # Check perimeter
    def test_perimeter_pass_1(self):
        self.assertEqual(perimeter(34, 23), 114)
    def test_perimeter_pass_2(self):
        self.assertEqual(perimeter(23, 4325235), 8650516)
    
    def test_perimeter_value_error_1(self):
        with self.assertRaises(ValueError):
            perimeter(4357, 0)
    def test_perimeter_value_error_2(self):
        with self.assertRaises(ValueError):
            perimeter(432, -4234234)
    
    def test_perimeter_type_error_1(self):
        with self.assertRaises(TypeError):
            perimeter(234, '36')
    def test_perimeter_type_error_2(self):
        with self.assertRaises(TypeError):
            perimeter("235743", 164)