def area(a, b):
    ''' 
    Возвращает площадь прямоугольника
        
        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемое значение:
            area (int): площадь прмоугольника со сторонами a и b
        
        Пример:
            area(5, 3) вернет 15
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Side cannot be negative")
    return a * b

def perimeter(a, b): 
    '''
    Возвращает периметер прямоугольника
        
        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемое значение:
            perimeter (int): периметер прямоугольника со сторонами a и b
        
        Пример:
            perimeter(5, 3) вернет 16
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Side cannot be negative")
    return 2 * (a + b) 
