# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
  
# Описание проекта
Этот проект представляет собой набор функций для вычисления площади и периметра четырех различных геометрических фигур: квадрата, прямоугольника, треугольника и круга. Эти функции могут быть использованы для выполнения расчетов в различных приложениях, где требуется определить характеристики указанных фигур.

# Код программы на языке python с примерами вывода

## Circe
~~~python
import math

def area(r):
    '''  Принимимает радиус круга, возвращает его площадь   '''
    return math.pi * r * r

def perimeter(r):
    '''  Принимает радиус круга, возвращает его периметр   '''
    return 2 * math.pi * r

### Пример работы программы
print(area(10))
print(perimeter(10))
314.1592653589793
62.83185307179586
~~~

## Rectangle
~~~python
def area(a, b):
    ''' Принимает длины сторон прямоугольника, возвращает его площадь '''
    return a * b

def perimeter(a, b):
    ''' Принимает длины сторон прямоугольника, возвращает его периметр '''
    return  2 * (a + b)

### Пример работы программы
print(area(10, 5))
print(perimeter(10, 7))
50
34
~~~

## Square
~~~python
def area(a):
    ''' Принимает длину стороны квадрата, возвращает его площадь'''
    return a * a


def perimeter(a):
    ''' Принимает длину стороны квадрату, возвращает его периметр'''
    return 4 * a

### Пример работы программы
print(area(10))
print(perimeter(10))
100
40
~~~

## Triangle
~~~python
def area(a, h):
    ''' Принимает длину основания и высоту треугольника, возвращает его площадь'''
    return a * h / 2

def perimeter(a, b, c):
    ''' Принимает длины трёх сторон треугольника, возвращает его периметр'''
    return a + b + c

### Пример работы программы
print(area(10, 3))
print(perimeter(10, 6, 7))
15
23
~~~

# История изменений с выводом хешей коммитов
~~~
68fdae4 documentation to triangle.py was added
1006009 documentation to square.py was added
bde3cd2 documentation to rectangle.py was added
a4ef22f documention to circle.py was added
bfeb8db  error from rectangle.py was fixed
dfc562d triangle was added + error from rectangle was fixed
e786cb7 rectangle was added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
~~~
