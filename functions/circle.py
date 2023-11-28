import math

def area(r):
    '''Функция для вычисления площади круга.
 
         Args:
             r (float): Радиус круга.

         Returns:
             float: Площадь круга.
         Example of call:
            result = area(3.0)
            print(result)  # Выведет: 28.274333882308138'''
    if r<0:
        return 0
    return math.pi * r * r


def perimeter(r):
    '''Функция для вычисления длины круга.
 
         Args:
             r (float): Радиус круга.

         Returns:
             float: Длина круга.
         Example of call:
            result = (3.0)
            print(result)  # Выведет: 18.84955592153876'''
    if r<0:
        return 0
    return 2 * math.pi * r

