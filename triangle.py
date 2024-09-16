def area(a, h): 
    ''' Принимает высоту и основание треугольника, возвращает его площадь. 
     
        Пример вызова:
            Принимаемое значение: 2, 3 (a, h)
            Возвращаемое значение: 3 (a * h / 2)
    '''
    if type(a) == str or type(h) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(h) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (h == 0):
        return "Error: Zero Length"

    if (a < 0) or (h < 0):
        return "Error: Negative Length"
        
    return a * h / 2 

def perimeter(a, b, c): 
    ''' Принимает 3 стороны треугольника, возвращает его периметр. 
    
        Пример вызова:
            Принимаемое значение: 2, 3, 4 (a, b, c)
            Возвращаемое значение: 9 (a + b + c)
    '''
    if type(a) == str or type(b) == str or type(c) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float or type(c) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0) or (c == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0) or (c < 0):
        return "Error: Negative Length"
        
    return a + b + c 

