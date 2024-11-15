import unittest

def area(a):
    '''
    Возвращает площадь квадрата
        Входные данные:
        a (int) - длина ребра квадрата
        
        Выходные данные:
        area (int) - площадь квадрата
        
        Пример:
            area(5) - вернёт 25
    '''
    if not isinstance(a, int):
        raise TypeError("Сторона квадрата должна быть целым числом")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше 0")
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата
        Входные данные:
        a (int) - длина ребра квадрата
        
        Выходные данные:
        perimeter (int) - периметр квадрата
        
        Пример:
            area(5) - вернёт 20
    '''
    if not isinstance(a, int):
        raise TypeError("Сторона квадрата должна быть целым числом")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше 0")
    return 4 * a

class SquareTests(unittest.TestCase):
    # Check area
    def test_area_pass_1(self):
        self.assertEqual(area(4), 16)
    def test_area_pass_2(self):
        self.assertEqual(area(6342645421), 40229150936532267241)
    
    def test_area_value_error_1(self):
        with self.assertRaises(ValueError):
            area(0)
    def test_area_value_error_2(self):
        with self.assertRaises(ValueError):
            area(-56235552)
    
    def test_area_type_error_1(self):
        with self.assertRaises(TypeError):
            area('4')
    def test_area_type_error_2(self):
        with self.assertRaises(TypeError):
            area("5423529")
    
    # Check perimeter
    def test_perimeter_pass_1(self):
        self.assertEqual(perimeter(72), 288)
    def test_perimeter_pass_2(self):
        self.assertEqual(perimeter(6346723), 25386892)
    
    def test_perimeter_value_error_1(self):
        with self.assertRaises(ValueError):
            perimeter(0)
    def test_perimeter_value_error_2(self):
        with self.assertRaises(ValueError):
            perimeter(-7542546)
    
    def test_perimeter_type_error_1(self):
        with self.assertRaises(TypeError):
            perimeter('52384')
    def test_perimeter_type_error_2(self):
        with self.assertRaises(TypeError):
            perimeter("72313==3?sg33473")