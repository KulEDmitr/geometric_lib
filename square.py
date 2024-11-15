def area(a):
    '''Принимает число a (сторона квадрата), возвращает площадь квадрата'''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "Incorrect input"
    return a * a

    '''
    Пример: area(10) == 100
    '''

def perimeter(a):
    '''Принимает число a (сторона квадрата), возвращает периметр квадрата'''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "Incorrect input"
    return 4 * a

    '''
    Пример: perimeter(10) == 40
    '''
