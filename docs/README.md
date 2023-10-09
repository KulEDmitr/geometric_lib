# Geometric_lib
Geometric_Lib предоставляет возможность работать со следующими геометрическими фигурами:
- [Круг](https://github.com/Artem010999/geometric_lib#Круг)
- [Квадрат](https://github.com/Artem010999/geometric_lib#Квадрат)
- [Прямоугольник](https://github.com/Artem010999/geometric_lib#КПрямоугольник)
- [Треугольник](https://github.com/Artem010999/geometric_lib#Треугольник)

# Круг
Ссылка на [код](https://github.com/Artem010999/geometric_lib/blob/main/circle.py) 
```python
import math 

def area(r): # Возвращает площадь круга
    return math.pi * r * r

Input: 7
Output: 153.93804002589985
```

```python
import math

def perimeter(r): # Возвращает периметр круга
    return 2 * math.pi * r

Input: 10
Output: 62.83185307179586
```

# Квадрат
Ссылка на [код](https://github.com/Artem010999/geometric_lib/blob/main/square.py)
```python
def area(a): # Возвращает площадь квадрата
    return a * a

Input: 11
Output: 121
```

```python
def perimeter(a, b): # Вовзвращает периметр квадрата
    return 4 * a

Input: 4
Output: 16
```

# Прямоугольник
Ссылка на [код](https://github.com/Artem010999/geometric_lib/blob/main/rectangle.py)
```python
def area(a, b): # Возвращает площадь прямоугольника
    return a * b

Input: 5, 10
Output: 50
```

```python
def perimeter(a, b): # Вовзвращает периметр прямоугольника
    return (a + b) * 2

Input: 2, 6
Output: 16
```

```python
def diagonal(a, b): # Возвращает диагональ прямоугольника
	return (a ** 2 + b ** 2) ** 0.5

Input: 3, 4
Output: 5

```

# Треугольник
Ссылка на [код](https://github.com/Artem010999/geometric_lib/blob/main/triangle.py)
```python
def area(a, h): # Возвращает площадь треугольника
	return a * h / 2

Input: 5, 4
Output: 10
```

```python
def perimeter(a, b, c): # Вовзвращает периметр треугольника
    return a + b + с

Input: 6, 8, 10
Output: 24
```

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Diagonal
- Rectangle: c = √(a² + b²)
