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

def area(r): // input: 3
    // Принимает число r и возвращает площадь круга радиусом r
	return pi * r * r // output: 28.27433388

def perimeter(r): // input 50
    // Принимает число r и возвращает периметр окружности радиусом r
    return pi * r * 2 // output 314.15926535
```

## Треугольник
```
def area(a, h): // input: (4, 10)
    // Принмает a, h, возвращает площадь треугольника с стороной a, и высотой опущенной к этой стороне h
    return a * h / 2 // output: 20

def perimeter(a, b, c): // input: (3, 4, 5)
	//принимает a, b, c, возвращает периетр треугольника с сторонами a, b, c    
	return a + b + c // output: 12
```
## Прямоугольник
```
def area(a, b): // input: (52,4)
	// Принимает a, b возвращает площадь прямоугольника с сторонами a, b
    return a * b // output: 208

def perimeter(a, b): // input: (24,42)
    // Принимает a, b возвращает периметр прямоугольника с сторонами a, b
    return 2 * (a + b) // output: 132
```

## Квадрат
```
def area(a): // input: 4
    // Принимает а, возвращает площадь квадрата стороной а
    return a * a // output: 16

def perimeter(a): // input: 15
    // Принимает а, возвращает периметр квадрата стороной а
    return 4 * a // output: 60
```
## История коммитов
![commits](https://raw.githubusercontent.com/Osaulenko-I/geometric_lib/a9696feeb2bf90e680b3691bdf331b44e5b8859d/commit%20history.png)
