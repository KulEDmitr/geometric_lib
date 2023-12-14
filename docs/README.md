# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Функций возвращающие значения,Math formulas

## Общее описание
- Данные функции вычисляют площадь и периметр для представленых выше фигур
- Для каждой фигуры свой файл,где содержатся функции вычисляющие
их площадь и периметр

### circle.py
``` python 
import math

#вызывает библиотеку math

def area(r):
    '''
        принимает цулое число r ,предполагаемый радиус окружности
        возвращает значение площади с плавающей точкой
        r(5) = pi * 5 * 5 = 78,5398
    '''
    return math.pi * r * r

def perimeter(r):
    '''
        принимает целое r ,предполагаемый радиус окружности
        возвращает значение периметра с плавающей точкой
        r(5) = 2 * pi * r = 31,4159265359
    '''
    return 2 * math.pi * r
```
### rectangle.py
``` python
def area(a, b):
    '''
        принимает целое число a и целое число b = стороны прямоугольника
        возвращает значение площади целое число
        a(10) b(2) = a * b = 20
    '''
    return a * b
def perimeter(a, b):
    '''
        принимает целое число a и целое число b = стороны прямоугольника
        возвращает значение периметра целое число
        a(10) b(2) = 2*(a+b) = 24
    '''
    return 2*(a + b)
```
### square.py
``` python
def area(a):
    '''
        принимает целое число a  =  сторона квадрата
        возвращает значение площади целое число
        a (4) = a*a =16
    '''
    return a * a
    
def perimeter(a):
    '''
        принимает целое число a  =  сторона квадрата
        возвращает значение периметра целое число
        a(4)=a*4 = 16
    '''
    return 4 * a
```
### triangle.py
``` python
def area(a, h):
    '''
        принимает целое число a и целое число h = сторона и высота треугольника
        возвращает значение площади целое число
        a(2) h(3) = a * h /2= 3
    '''
    return a * h / 2
    
def perimeter(a, b, c):
    '''
        принимает целое число a и целое число b и целое число c = стороны треугольника
        возвращает значение периметра целое число
        a(10) b(10) c(10) = a+b+c = 30
    '''
    return a + b + c
    
```
### Fix rectangle.py and add triangle.py

> Thu Sep 7 10:29:13 2023 +0300, commit hash:
[17fad60351c9b4046bd398486fe6da5d9fab3662](https://github.com/hashlag/geometric_lib/commit/17fad60351c9b4046bd398486fe6da5d9fab3662)

- Добавлены функции для работы с треугольниками, исправлена ошибка в файле `triangle.py`

### Add rectangle.py

> Thu Sep 7 10:22:57 2023 +0300, commit hash:
[407db5bf4636a856f91eaf2868a9f2dc0994d68a](https://github.com/hashlag/geometric_lib/commit/407db5bf4636a856f91eaf2868a9f2dc0994d68a)

- Добавлены функции для работы с прямоугольниками

### Add unittest
- Добавлены Unittests для каждого файла
- Создан файл TESTS.py где расположен код всех тетов
#### Данные для тестов
``` python
first: 1 2 3 4 5 6 7 
second: 10 10 10 10 10 10 10
third: 32 43 23 82 47 12 21
expectation: Ran 12 tests in 10,9]s
Ok
```