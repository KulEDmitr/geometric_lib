def area(a, h): 
    
    '''
    Принимает число a, h (основание и высота треугольника) возвращает площадь треугольника
    
    Example:
    Input: 1 2
    Output: 1
    
    '''
    
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)) or a < 0 or h < 0 or a > 10**10 or h > 10**10:
        return "wrong input"
    
    return a * h / 2 
def perimeter(a, b, c): 
    '''
    Принимает число a, b, c (стороны треугольника), возвращает периметр треугольника
    
    Example:
    Input: 1 2 3
    Output: 6
    
    '''
    
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or a < 0 or b < 0 or c < 0 or a > 10**10 or b > 10**10 or c > 10**10:
        return "wrong input"
    
    
    return a + b + c
