# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Геометрические Функции на Python

## Общее описание решения

Этот проект содержит функции для вычисления площади и периметра квадратов и кругов. Он предназначен для упрощения расчетов в геометрии, предоставляя удобные методы для вычисления основных характеристик этих фигур. Все функции принимают параметры в виде целых или вещественных чисел и возвращают соответствующие значения.

## Описание функций
### 1. Площадь квадрата

```
def area(a)
    '''
    Площадь квадрата

    Args:
        a (int or float): сторона квадрата

    Returns:
        int or float: площадь квадрата

    Examples:
        >>> area(4)
        16
        >>> area(3.5)
        12.25
    '''
    return a * a
```
### 2. Периметр квадрата
```
def perimeter(a):
    '''
    Периметр квадрата

    Args:
        a (int): сторона квадрата

    Returns:
        int or float: периметр квадрата

    Examples:
        >>> perimeter(5)
        20
        >>> perimeter(3.5)
        14
    '''
    return 4 * a
```
### 3. Площадь круга
```
import math


def area(r):
    '''
    Принимает на вход радиус и возвращает площадь круга

    Args:
        r (int or float): радиус круга

    Returns:
        int or float: площадь круга

    Examples:
        >>> area(7)
        153.93804002589985
        >>> area(2.5)
        19.634954084936208
    '''
    return math.pi * r * r
```
### 4. Периметр круга
```
import math


def perimeter(r):
    '''
    Принимает на вход радиус и возвращает периметр круга

    Args:
        r (int or float): радиус круга

    Returns:
        int or float: площадь круга

    Examples:
        >>> perimeter(6)
        37.69911184307752
        >>> perimeter(3.6)
        22.61946710584651
    '''
    return 2 * math.pi * r
```
### 5. Площадь прямоугольника
```
def area(a, b):
    '''
    Принимает на вход стороны a и b, возвращает площадь прямоугольника

    Args:
        a, b (int or float): стороны прямоугольника

    Returns:
        int or float: площадь прямоугольника

    Examples:
        >>> area(3, 4)
        12
        >>> area(2.5, 4)
        10
    '''
    return a * b
```
### 6. Периметр прямоугольника
```
def perimeter(a, b):
    '''
    Принимает на вход стороны а и b, возвращает периметр прямоугольнка

    Args:
        a, b (int or float): стороны прямоугольника

    Returns:
        int or float: периметр прямоугольника

    Examples:
        >>> perimeter(1, 7)
        16
        >>> perimeter(2.5, 7)
        19
    '''
    return (a + b) * 2
```
### 7. Площадь треугольника
```
def area(a, h):
    '''
    Принимает на вход сторону а и высоту h, возвращает площадь треугольника

    Args:
        a, h (int or float): стороны и высота треугольника

    Returns:
        int or float: площадь треугольника

    Examples:
        >>> area(6, 7)
        21
        >>> area(2, 3)
        3
    '''
    return a * h / 2
```
### 8. Периметр треугольника
```
def perimeter(a, b, c):
    '''
    Принимает на вход 3 стороны треугольника

    Args:
        a, b, c (int or float): стороны треугольника

    Returns:
        int or float: площадь треугольника

    Examples:
        >>> perimeter(3, 4, 5)
        12
        >>> perimeter(1.5, 2, 5)
        8.5
    '''
    return a + b + c
```

## Установка и использование
Для использования функций просто скопируйте код в ваш Python-скрипт или импортируйте его в ваш проект.
## История изменений
``` 
"3c8d66ac5b4a3e2f1g0h9i8j7k6l5m4n3o2p1q0r" (HEAD -> new_features_466067) Mistake was fixed
"73e236cf4c5e6d7b8a9c0e1f2d3c4b5a6e7f8g9h" Added new file rectangle.py
"d078c8d9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p3" L-03: Docs added
"8ba9aebc0d1e2f3a4bbc6d2e8f9g0h1i2jek4l8m" L-03: Circle ans square added
```
