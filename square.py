
def area(a):
    ''' Принимает число a (сторону квадрата), возвращает площадь квадрата.
    
    Пример вызова:
            Принимаемое значение: 2 (a)
            Возвращаемое значение: 4 (a²)
    '''
    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"
        
    return a * a


def perimeter(a):
    ''' Принимает число а (сторону квадрата), возвращает периметр квадрата. 
    
    Пример вызова:
            Принимаемое значение: 2 (a)
            Возвращаемое значение: 8 (4 * a)
    '''
    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"
        
    return 4 * a
