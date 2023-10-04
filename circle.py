import math


def area(r):
    '''
    Принимает число r, возвращает произведение квадрата числа r на округлённое число π, используя функцию math.pi из библиотеки math
    Пример: r = 3. Фуркция вернёт число 28.274333882308138 (area(3) = 28.274333882308138)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает произведение числа 2 на число r и округлённое число π, используя функцию math.pi из библиотеки math
    Пример: r = 3. Фуркция вернёт число 18.84955592153876 (perimeter(3) = 18.84955592153876)
    '''
    return 2 * math.pi * r

