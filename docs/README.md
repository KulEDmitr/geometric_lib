# Общее описание решений
- Сделал git clone своего репозитория
- открыл папку geometric_lib через терминал
- Описал решение фаилов rectangle.py и triangle.py на Pycharm
- Сделал git commit каждому файлу
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
# Описание каждой функции с примерами вызова
## Circle:
```
import math
import unittest

def area_circle(r):
    '''Принимает число r-радиус окружности, возвращает её площадь'''
    return math.pi * r * r


def perimeter_circle(r):
    '''Принимает число r-радиус окружности, возвращает её длину'''
    return 2 * math.pi * r
```

_Example:_

in : `10`
out :` 100   62,83`

## Rectangle:
```
def area_rectangle(a, b):
    """Получает на вход боковую сторону a и основание прямоугольника b, возвращает его площадь"""
    return a * b

def perimeter_rectangle(a, b):
    """Получает на вход боковую сторону a и основание прямоугольника b, возвращает его периметр"""
    return 2*(a + b)
```
_Example:_

in: `3    4`
out : `12      14`

## Square:
```
def area_square(a):
    """Принимает сторону квадрата a, возвращает его площадь"""
    return a * a

def perimeter_square(a):
    """Принимает сторону квадрата a, возвращает его периметр"""
    return 4 * a

   ```

_Example:_

in : `10 `
out : `100     40`

## Triangle :
```
def area_triangle(a, h):
    """
    Принимает сторону треугольника a и высоту h, опирающуюся на сторону a,
    возвращает площадь треугольника
    """
    return a * h / 2

def perimeter_triangle(a, b, c):
    """Принимает стороны треугольника a,b,c, возвращает его периметр"""
    return a + b + c
```

_Example:_

in : `10 5`       `3 3 4 `
out : `25     10`

# История изменения проекта с хешами комитов
1. **commit** 5e01bedbd8701b0801affa857b64b303f8105e38
```
 Author: Nguyen Van Chinh <nvchinh23022004@gmail.com>
 Date:   Fri Oct 4 13:25:18 2024 +0300

   adding comment to circle.py
```
2. **commit** 5e97c4b409bd2462994af4cb4195f48091d2fc43
```
 Author: Nguyen Van Chinh <nvchinh23022004@gmail.com>
 Date:   Fri Oct 4 13:24:19 2024 +0300

     adding comment to square.py
```
3. **commit** c771d335aa477310db4d053780ad2ec484808148
```
 Author: Nguyen Van Chinh <nvchinh23022004@gmail.com>
 Date:   Fri Oct 4 13:23:03 2024 +0300

     adding comment to triangle.py
```
4. **commit** 35b21816d0bcdd156bd79b185342f6c9315790e2
```
Author: Nguyen Van Chinh <nvchinh23022004@gmail.com›
Date:    Fri Oct 4 13:22:05 2024 +0300
    adding comment to rectangle. py
```
