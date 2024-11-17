def area_square(a):
    '''Принимает сторону квадрата a, возвращает его площадь
    Example:

    in : `10 `
    out : `100 `
    '''
    # Проверка на корректность ввода
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "Incorrect input"
    return a * a

def perimeter_square(a):
    '''Принимает сторону квадрата a, возвращает его периметр
    Example:

    in : `10 `
    out : `  40`
     '''
    if not isinstance(a, (int, float)) or a < 0 or a > 10**10:
        return "Incorrect input"
    return 4 * a
