def area(a, h): 
    '''
    Возвращает площадь треугольника
        Входные данные:
        a (int) - длина основание треугольника
        h (int) - высота к основанию a
        
        Выходные данные:
        area (int) - площадь Треугольник
        
        Пример:
            area(5, 10) - вернёт 25
    '''
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
    return a + b + c 