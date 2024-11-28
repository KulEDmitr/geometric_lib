def area(a):
    '''
    Принимает число a (сторона квадрата), возвращает площадь  квадрата
    
    Example:
    Input: 3
    Output: 9
    
    '''
    
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "wrong input"
    
    return a * a

def perimeter(a):
    '''
    Принимает число a (сторона квадрата), возвращает периметр квадрата
    
    Example:
    Input: 3
    Output: 12
    
    '''
    
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "wrong input"
    
    return 4 * a
