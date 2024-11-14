def area(a, h):
    ''' 
    Возвращает площадь треугольника
        
        Параметры:
            a (int): основание треугольника
            h (int): высота треугольника

        Возвращаемое значение:
            area (int): площадь прмоугольника с основанием a и высотой h
        
        Пример:
            area(5, 4) вернет 10
    '''
    if a <= 0 or h <= 0:
        raise ValueError("Height or side cannot be negative")
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметер треугольника
        
        Параметры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника

        Возвращаемое значение:
            perimeter (int): периметер треугольника со сторонами a, b, c
        
        Пример:
            perimeter(2, 3, 4) вернет 9
    '''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive values")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid side lengths for a triangle")
    return a + b + c
