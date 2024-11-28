
def area(a, b): 
    '''
    Принимает число a и b (длина и ширина прямоугольника), возвращает площадь  прямоугольника
    
    Example:
    Input: 5 6
    Output: 30

    '''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "wrong input"
    
    return a * b 

def perimeter(a, b): 
    '''
    Принимает число a и b (длина и ширина прямоугольника), возвращает периметр прямоугольника
    
    Example:
    Input: 5 6
    Output: 22
    
    '''
    
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "wrong input"
    
    return (a + b)*2
    
    