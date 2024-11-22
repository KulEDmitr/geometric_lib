def area(a, b): 
    '''Принимает две стороны прямоугольника и возвращает его площадь
        Пример: возьмем a = 2, b = 3, тогда area(2, 3) вернет значение - 6'''

    if a < 0 or b < 0:
        raise ValueError("--Сторона прямоугольника не может быть отрицательной--")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a * b 

def perimeter(a, b):
    '''Принимает две стороны прямоугольника и возвращает его периметр
        Пример: возьмем a = 5, b = 6, тогда perimeter(5, 6) вернет значение - 22'''

    if a < 0 or b < 0:
        raise ValueError("--Сторона прямоугольника не может быть отрицательной--")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return 2 * (a + b)
