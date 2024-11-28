def area_triangle(a, h):
    '''
    Принимает сторону треугольника a и высоту h, опирающуюся на сторону a,
    возвращает площадь треугольника
    Example:

    in : `10 5 `
    out : `25 `
    '''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)) or a < 0 or h < 0 or a > 10**10 or h > 10**10:
        return "Incorrect input"
    return a * h / 2

def perimeter_triangle(a, b, c):
    '''Принимает стороны треугольника a,b,c, возвращает его периметр
    Example:

    in : 
    `3 3 4 `
    out : ` 10`
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or a < 0 or b < 0 or c < 0 or a > 10**10 or b > 10**10 or c > 10**10:
        return "Incorrect input"
    return a + b + c