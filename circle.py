import math
def area_circle(r):
    '''
    Принимает число r-радиус окружности, возвращает её площадь
    
    Example:
        in : `10`
        out :` 100`
    '''
    # Проверка на корректность ввода
    if not isinstance(r, (int, float)) or r < 0 or r > 10**10:
        return "Incorrect input"
    return math.pi * r * r


def perimeter_circle(r):
    '''Принимает число r-радиус окружности, возвращает её длину
    Example:

    in : `10`
    out :` 62,83`
    '''
    # Проверка на корректность ввода
    if not isinstance(r, (int, float)) or r < 0 or r > 10**10:
        return "Incorrect input"
    return 2 * math.pi * r