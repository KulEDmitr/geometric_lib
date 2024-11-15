def area(a):
    '''Принимает сторону квадрата и возвращает его площадь
        Пример: возьмем a = 4, тогда area(4) вернет значение - 16'''

    if a < 0:
        raise ValueError("--Сторона квадрата не может быть отрицательной--")
    if type(a) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a * a


def perimeter(a):
    '''Принимает сторону квадрата и возвращает его периметр
        Пример: возьмем a = 2, тогда perimeter(2) вернет значение - 8'''

    if a < 0:
        raise ValueError("--Сторона квадрата не может быть отрицательной--")
    if type(a) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return 4 * a
