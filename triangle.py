def area(a, h): 
    '''Принимает сторону и высоту треугольника и возвращает его площадь
        Пример: возьмем a = 4, h == 2, тогда area(4, 2) вернет значение - 4'''

    if a < 0:
        raise ValueError("--Сторона треугольника не может быть отрицательной--")
    if h < 0:
        raise ValueError("--Высота треугольника не может быть отрицательной--")
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает стороны треугольника и возвращает его периметр
        Пример: возьмем a = 2, b = 3, c = 4, тогда perimeter(2, 3, 4) вернет значение - 9'''

    if a < 0 or b < 0 or c < 0:
        raise ValueError("--Сторона треугольника не может быть отрицательной--")
    if a + b < c or a + c < b or c + b < a:
        raise ValueError("--Треугольник с такими сторонами не может существовать--")
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a + b + c 
