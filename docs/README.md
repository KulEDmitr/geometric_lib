# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Поиск площади и периметра разных геометрических фигур
## Окружность
Для нахождения площади и периметра окружности для начала необходимо добавить число `pi`. Для этого нужно импортировать библиотеку `math`:  
```
import math
```  
Далее создаем функции:  
```
import math

def area(r):
	"""
	Принимает число r и возвращает площадь круга радиусом r
	Пример
	input: 3
	output: 28.27433388
	"""
	return pi * r * r

def perimeter(r):
	"""
	Принимает число r и возвращает периметр окружности радиусом r
	Пример
	input: 50
	output: 314.15926535
	"""
    return pi * r * 2
```

## Треугольник
```
def area(a, h):
	"""
	Принмает a, h, возвращает площадь треугольника с стороной a, и высотой опущенной к этой стороне h
	Пример
	input: 4, 10
	output: 20
	"""
	return a * h / 2

def perimeter(a, b, c):
	"""
	Принимает a, b, c, возвращает периетр треугольника с сторонами a, b, c
	input: 3, 4, 5  
	output: 12
	"""
	return a + b + c
```
## Прямоугольник
```
def area(a, b):
 	"""
 	Принимает a, b возвращает площадь прямоугольника с сторонами a, b
 	Пример
 	input: 52, 4
 	output: 208
 	"""
	return a * b

def perimeter(a, b):
 	"""
 	Принимает a, b возвращает периметр прямоугольника с сторонами a, b
 	Пример
 	input: 4, 10
 	output: 28
 	"""
    	return 2 * (a + b)
```

## Квадрат
```
def area(a):
    """
    Принимает а, возвращает площадь квадрата стороной а
    Пример
    input: 4
    output: 16  
    """
    return a * a

def perimeter(a):
    """
    Принимает а, возвращает периметр квадрата стороной а
    Пример
    input: 15
    output: 60
    """
    return 4 * a
```
## История коммитов
![commits](https://raw.githubusercontent.com/Osaulenko-I/geometric_lib/a9696feeb2bf90e680b3691bdf331b44e5b8859d/commit%20history.png)
### Sep 27, 2024
[commit](https://github.com/Osaulenko-I/geometric_lib/commit/f25e9be9a4b7bd93d5a9e105be7bff4db00871c6), rect fix and trian add  
[commit](https://github.com/Osaulenko-I/geometric_lib/commit/d3d3f4a32ba2bae5071abf927882f1a83ddf8236), add rectange
### Mar 4, 2021
[commit](https://github.com/Osaulenko-I/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2), L-03: Docs added  
[commit](https://github.com/Osaulenko-I/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460), L-03: Circle and square added
