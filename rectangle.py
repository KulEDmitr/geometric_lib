def area(a, b): 
    '''
    Принимает числа a и b (стороны прямоугольника), возвращает произведение чисел a и b (площадь прямоугольника)

    Пример вызова функции:
        Входное значение a, b (int/float, int/float): 5, 6
        Возвращаемое значение area (int/float): 30
    '''
    
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Error: the function is not passed an int/float type")
    if  a <= 0 or b <= 0:
        raise ValueError("Error: one of the numbers less than 0 or equal 0")
    
    return a * b 


def perimeter(a, b): 
    '''
    Принимает числа a и b (стороны прямоугольника), возвращает удвоенную сумму чисел a и b (периметр прямоугольника)

    Пример вызова функции:
        Входное значение a, b (int/float, int/float): 5, 6
        Возвращаемое значение area (int/float): 22
    '''

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Error: the function is not passed an int/float type")
    if  a <= 0 or b <= 0:
        raise ValueError("Error: one of the numbers less than 0 or equal 0")
    
    return 2*(a + b) 
