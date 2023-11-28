
def area(a, h):
    '''Функция для вычисления площади треугольника.
 
         Args:
             a (float): Первая сторона треугольника.
             h (float): Вторая сторона треугольника.
         Returns:
             float: Площадь треугольника.
         Example of call:
            result = area(7.77, 6.66)
            print(result)  # Выведет: 25.8741'''
    if a<0 or h<0:
        return 0
    return a * h / 2

def perimeter(a, b, c):
    '''Функция для вычисления периметра треугольника.
 
         Args:
             a (float): Первая сторона треугольника.
             b (float): Вторая сторона треугольника.
             c (float): Третья сторона треугольника.

         Returns:
             float: Периметр треугольника.
         Example of call:
            result = area(7.77, 6.66, 2.28)
            print(result)  # Выведет: 16.71'''
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        return a + b + c
    return 0
