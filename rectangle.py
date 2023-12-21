def area(a, b):
    ''' Принимает числа a и b (стороны прямоугольника), возвращает площадь прямоугольника. 
    
    Пример вызова:
            Принимаемое значение: 2, 3 (a, b)
            Возвращаемое значение: 6 (a * b)
    '''
    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"
        
    return a * b
    
def perimeter(a, b):
    ''' Принимает числа a и b (стороны прямоугольника), возвращает периметр прямоугольника. 
    
    Пример вызова:
            Принимаемое значение: 2, 3 (a, b)
            Возвращаемое значение: 10 (2 * a + 2 * b)
    '''
    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"
        
    return (a + b) * 2
    
