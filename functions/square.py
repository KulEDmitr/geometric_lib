
def area(a):
    '''Функция для вычисления площади квадрата.
 
         Args:
             a (float): Длина стороны квадрата.

         Returns:
             float: Площадь квадрата.
         Example of call:
            result = area(7.77)
            print(result)  # Выведет: 60.3729'''
    if a<0:
        return 0
    return a * a


def perimeter(a):
    '''Функция для вычисления периметра квадрата.
 
         Args:
             a (float): Длина стороны квадрата.

         Returns:
             float: Периметр квадрата.
         Example of call:
            result = area(7.77)
            print(result)  # Выведет: 31.08'''
    if a<0:
        return 0
    return 4 * a
