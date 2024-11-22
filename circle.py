import math


def area(r):
    '''
    Вычисляет и возвращает площадь круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    area_circle (float): площадь круга, вычесленная по формуле area_circle = pi * r ^ 2

            Пример вызова:
                Входные данные: 2.0
                Результат: 12.56636
    '''

    area_circle =  math.pi * r * r
    return area_circle

def perimeter(r):
    '''
    Вычисляет и возвращает периметр круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    perimetr_circle (float): периметр круга, вычесленный по формуле perimeter_circle = 2 * pi * r

            Пример вызова:
                Входные данные: 2.0
                Результат: 12.56636
    '''
    perimetr_circle = 2 * math.pi * r
    return perimetr_circle

