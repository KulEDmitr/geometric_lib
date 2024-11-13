def area(a, h): 
    '''
    Принимает числа a и h (a - одна из сторон треугольника, h - высота, проведенная к этой стороне), возвращает половину произведения чисел a и h (площадь треугольника)

    Пример вызова функции:
        Входное значение a, h (int/float, int/float): 5, 6
        Возвращаемое значение area (int/float): 15
    '''

    if not (isinstance(a, (int, float)) and isinstance(h, (int, float))):
        raise TypeError("Error: the function is not passed an int/float type")
    if  a <= 0 or h <= 0:
        raise ValueError("Error: one of the numbers less than 0 or equal 0")
    
    return a * h / 2 


def perimeter(a, b, c): 
    '''
    Принимает числа a, b, c (стороны треугольника), возвращает сумму чисел a, b, c (периметр треугольника)

    Пример вызова функции:
        Входное значение a, b, c (int/float, int/float, int/float): 5, 6, 7
        Возвращаемое значение area (int/float): 18
    '''
    
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError("Error: the function is not passed an int/float type")
    if  a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Error: one of the numbers less than 0 or equal 0")
    if (a+b <= c) or (a+c <= b) or (b+c <= a):
         raise ValueError("Error: there is no triangle with sides a,b,c")
    return a + b + c 
