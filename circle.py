import math
'''Подключит библиотеку math'''

def area(r):
    '''
    Принимает число r (радиус круга), возвращает площадь круга
    
    Example:
    Input: 4
    Output: 50.26548245743669
    
    '''
    # Проверка на корректность ввода
    if not isinstance(r, (int, float)) or r < 0 or r > 10**10:
        return "wrong input"
    
    
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r (радиус круга), возвращает периметр круга
    
    Example:
    Input: 4
    Output: 25.132741228718345
    
    '''
    # Проверка на корректность ввода
    if not isinstance(r, (int, float)) or r < 0 or r > 10**10:
        return "wrong input"
    
    return 2 * math.pi * r
