import math

'''импортируем библиотеку math, для получения числа пи'''

def circ_area(r):
    '''
    Принимает число r, возвращает его квадрат, умноженный на число пи

        Параметры:
            r (int, float, etc...) первое число

        Вовзращаемое значение:
            a_squres_multiplied_by_pi (float, etc...) квадрат числа r, умноженный на число пи

    Пример вызова функции:
    input >> 3
    output << 28.274333882308138
    '''
    if r < 0:
        return "Wrong input parameters"
    return math.pi * r * r



def circ_perimeter(r):
    '''
    Принимает число r, возвращает его, умноженное на удвоенное число пи

        Параметры:
            r (int, float, etc...) первое число

        Вовзращаемое значение:
            a_multiplied_by_double_pi (float, etc...) число r, умноженное на удвоенное число пи

    Пример вызова функции:
    input >> 2
    output << 12.566370614359172
    '''
    if r < 0:
        return "Wrong input parameters"
    return 2 * math.pi * r
