def area(a, b):
    '''Принимает числа a и b (стороны прямоугольника), возвращает площадь прямоугольника'''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "Incorrect input"
    return a * b

    '''
    Пример: area(2, 3) == 6
    '''

def perimeter(a, b):
    '''
    Принимает числа a и b (стороны прямоугольника), возвращает периметр прямоугольника
    '''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "Incorrect input"
    return 2 * (a + b)

    '''
    Пример: perimeter(2, 3) == 10
    '''