# Math formulas
# Общее описание проэкта
Поэкт на языке python для определения площади и периметра круга, прямоугольника, квадрата и треугольника. Используется библиотека math.
## Area
- circle: S = πR²
- cectangle: S = ab
- square: S = a²
- triangle: S = ah/2

## Perimeter
- circle: P = 2πR
- rectangle: P = 2a + 2b
- square: P = 4a
- triangle: P = a + b + c

## circle
``` python
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
```

## rectangle
``` python
def area(a, b):
    '''
    Аргументы функции: число a, число b
    Возвращаемое значение: произведение чисел a и b
    Пример 1: a = 2, b = 3. Функция вернёт число 6 (area(2, 3) = 6)
    Пример 2: a = 2, b = 2.5. Функция вернёт число 5.0 (area(2, 2.5) = 5.0)
    '''
    return a * b 

def perimeter(a, b):
    '''
    Аргументы функции: число a, число b
    Возвращаемое значение: сумма произведения числа 2 и числа a и произведения числа 2 и числа b
    Пример: a = 2, b = 3. Функция вернёт число 10 (perimetr(2, 3) = 10)
    '''
    return 2*a + 2*b
```
## square
``` python
def area(a):
    '''
    Принимает число a, возвращает квадрат числа a
    Пример: r = 3. Фуркция вернёт число 9 (area(3) = 9)
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число a, возвращает произведение числа 4 и чиса a
    Пример: a = 3. Фуркция вернёт число 12 (perimetr(3) = 12)
    '''
    return 4 * a
```
## triangle
``` python
def area(a, h):
    '''
    Аргументы функции: число a, число h
    Возвращаемое значение: произведение числа a и половины от числа h
    Пример: a = 2, h = 4. Функция вернёт число 4 (area(2, 4) = 4)
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Аргументы функции: число a, число b, число c
    Возвращаемое значение: сумма чисел a ,b и c
    Пример: a = 2, b = 3, c = 5. Функция вернёт число 10 (perimetr(2, 3, 5) = 10)
    '''
    return a + b + c
```

## Хэши коммитов
- C:\lab\geometric_lib> git log --pretty=oneline
- 5f721dd071f4124cdc71a46b4ddc972d37a807a4 (HEAD -> main) Edit readme.md
- 5a158cb3290ff54be28d48ad90d9b79ae0766a87 (origin/main, origin/HEAD) Add triangle.py and fix formula
- 4aee411be56c3be948e5cc2cd148e0fed9d4abac Add rectangle.py
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added