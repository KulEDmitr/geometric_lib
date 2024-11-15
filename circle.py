import math
import unittest

def area(r):
    '''
    Возвращает площадь круга
        Входные данные:
        r (int||float) - радиус круга
        
        Выходные данные:
        area (float) - площадь круга
        
        Пример:
            area(10) - вернёт 314.16
    '''
    if not (isinstance(r, float) or isinstance(r, int)):
        raise TypeError("Радиус круга должен быть числом")
    if r <= 0:
        raise ValueError("Радиус круга должен быть больше 0")
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности
        Входные данные:
        r (int||float) - радиус круга
        
        Выходные данные:
        area (float) - площадь круга
        
        Пример:
            perimeter(10) - вернёт 62.83
    '''
    if not (isinstance(r, float) or isinstance(r, int)):
        raise TypeError("Радиус круга должен быть числом")
    if r <= 0:
        raise ValueError("Радиус круга должен быть больше 0")
    return 2 * math.pi * r

class CircleTests(unittest.TestCase):
    # Check area
    def test_area_pass_1(self):
        self.assertAlmostEqual(area(2), 12.566, places=2)
    def test_area_pass_2(self):
        self.assertAlmostEqual(area(999222), 3136706236976.575, places=2)
    
    def test_area_value_error_1(self):
        with self.assertRaises(ValueError):
            area(0)
    def test_area_value_error_2(self):
        with self.assertRaises(ValueError):
            area(-3214234)
    
    def test_area_type_error_1(self):
        with self.assertRaises(TypeError):
            area('1')
    def test_area_type_error_2(self):
        with self.assertRaises(TypeError):
            area("321")
    
    # Check perimeter
    def test_perimeter_pass_1(self):
        self.assertAlmostEqual(perimeter(4), 25.133, places=2)
    def test_perimeter_pass_2(self):
        self.assertAlmostEqual(perimeter(345346), 2169872.913, places=2)
    
    def test_perimeter_value_error_1(self):
        with self.assertRaises(ValueError):
            perimeter(0)
    def test_perimeter_value_error_2(self):
        with self.assertRaises(ValueError):
            perimeter(-4234234)
    
    def test_perimeter_type_error_1(self):
        with self.assertRaises(TypeError):
            perimeter('5')
    def test_perimeter_type_error_2(self):
        with self.assertRaises(TypeError):
            perimeter("2343")