def area(a, b):
    if (a <= 0 or b<= 0):
        raise ValueError('Wrong input')
    '''Принимает числа a, b, возвращает их произведение. Example: first side = 1, second side = 2 => S = 2'''
    return a * b 

def perimeter(a, b):
    if (a <= 0 or b<=0):
        raise ValueError('Wrong input')
    '''Принимает числа a, b, возвращает их удвоенную сумму. Example: first side = 1, second side = 2 => P = 6'''
    return a + b + a + b


