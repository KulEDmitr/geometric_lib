def area(a):
    '''
    Принимает число a (сторону квадрата), возвращает квадрат числа a (площадь квадрата)

    Пример вызова функции:
        Входное значение a (int/float): 5
        Возвращаемое значение area (int/float): 25
    '''
    
    if not isinstance(a, (int, float)): 
        raise TypeError("Error: the function is not passed an int/float type")
    if a <= 0:
        raise ValueError("Error: number less than 0 or equal 0")
    
    return a * a


def perimeter(a):
    '''
    Принимает число a (сторону квадрата), возвращает 4*a (периметр квадрата)

    Пример вызова функции:
        Входное значение a (int/float): 5
        Возвращаемое значение perimeter (int/float): 20
    '''
    
    if not isinstance(a, (int, float)): 
        raise TypeError("Error: the function is not passed an int/float type")
    if a <= 0:
        raise ValueError("Error: number less than 0 or equal 0")
    
    return 4 * a



