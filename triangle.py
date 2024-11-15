def area(a, h):
    '''Принимает число a и h (основание и высота треугольника), возвращает площадь треугольника'''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)) or a < 0 or h < 0 or a > 10**10 or h > 10**10:
        return "Incorrect input"
    return a * h / 2

    '''
    Пример: area(10, 5) == 25
    '''

def perimeter(a, b, c):
    '''Принимает три числа a, b, c (стороны треугольника), возвращает периметр треугольника'''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or a < 0 or b < 0 or c < 0 or a > 10**10 or b > 10**10 or c > 10**10:
        return "Incorrect input"
    return a + b + c

    '''
    Пример: perimeter(3, 4, 5) == 12
    '''