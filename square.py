def area(a):
    ''' 
    Возвращает площадь квадрата
        
        Параметры:
            a (int): сторона квадрата

        Возвращаемое значение:
            area (int): площадь квадрата со стороной a
        
        Пример:
            area(5) вернет 25
    '''
    if a <= 0:
        raise ValueError("Side cannot be negative")
    return a * a


def perimeter(a):
    '''
    Возвращает периметер квадрата
        
        Параметры:
            a (int): сторона квадрата

        Возвращаемое значение:
            perimeter (int): периметер квадрата со стороной a
        
        Пример:
            perimeter(5) вернет 20
    '''
    if a <= 0:
        raise ValueError("Side cannot be negative")
    return 4 * a
