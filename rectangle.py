def area(a, b): 
'''
Принимает числа a и b, возвращает площадь прямоугольника.
    Параметры:
        a (int): длина прямоугольника
        b (int): высота прямоугольника
    Возращаемое значение:
        Площадь прямоугольника
    Пример:
        area(4, 5) -> (4 * 5) = 20 
''' 
    return a * b 

def perimeter(a, b): 
'''
Принимает числа a и b, возвращает периметр прямоугольника.
    Параметры:
        a (int): длина прямоугольника
        b (int): высота прямоугольника
    Возращаемое значение:
        Периметр прямоугольника
    Пример:
        area(4, 5) -> 2 * (4 + 5) = 18 
''' 
    return 2 * (a + b)
