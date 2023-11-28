
def area(a, b):
    '''Функция для вычисления площади прямоугольника.
 
         Args:
             a (float): Длина прямоугольника.
             b (float): Ширина прямоугольника.

         Returns:
             float: Площадь прямоугольника.
         Example of call:
            result = area(7.77, 6.66)
            print(result)  # Выведет: 51.7482'''
    return a * b

def perimeter(a, b):
    '''Функция для вычисления периметра прямоугольника.
 
         Args:
             a (float): Длина прямоугольника.
             b (float): Ширина прямоугольника.

         Returns:
             float: Периметр прямоугольника.
         Example of call:
            result = area(7.77, 6.66)
            print(result)  # Выведет: 28.86'''
    return 2 * (a + b)
