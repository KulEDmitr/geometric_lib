def area(a, h):
    """Принимает сторону и высоту треугольника (int, int)
        возвращает его площадь (float)

        print(area(4, 2)) -- > 4.0"""
    return a * h / 2

def perimeter(a, b, c):
    """Принимает 3 стороны треугольника (int, int, int)
        возвращает его периметр (int)

        print(perimeter(3, 4, 5)) -- > 12"""
    return a + b + c
