def area_rectangle(a, b):
    '''Получает на вход боковую сторону a и основание прямоугольника b, возвращает его площадь
    Example:

    in: `3    4`
    out : ` 12`
    '''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "Incorrect input"
    return a * b

    return a * b

def perimeter_rectangle(a, b):
    '''Получает на вход боковую сторону a и основание прямоугольника b, возвращает его периметр
    Example:

    in: `3    4`
    out : `14`

    '''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > 10**10 or b > 10**10:
        return "Incorrect input"
    return 2*(a + b)