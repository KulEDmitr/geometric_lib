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


# Описание каждой функции с примерами вызова

## Circle
- Функция нахождения площади, принимает на вход одно число, радиус круга, а возвращает его площадь т.e. число пи умноженное на квадрат радиуса.
```python
from geometric_lib import circle
circle.area(4)
// 50.26548245743669
```
- Функция нахождения периметра, принимает на вход одно число, радиус круга, а возвращает его периметр т.e. число пи умноженное на радиус и умноженное на 2.
```python
from geometric_lib import circle
circle.perimeter(4)
// 25.132741228718345
```

## Rectangle
- Функция нахождения площади, принимает на вход два числа, две стороны прямоугольника, а возвращает его площадь т.e. произведение сторон.
```python
from geometric_lib import rectangle
rectangle.area(2, 4)
// 8
```
- Функция нахождения периметра, принимает на вход два числа, две стороны прямоугольника, а возвращает его периметр т.e. удвоенная сумма сторон.
```python
from geometric_lib import circle
rectangle.perimeter(2, 4)
// 12
```

## Square
- Функция нахождения площади, принимает на вход одно число, сторону квадрата, а возвращает его площадь т.e. квадрат стороны.
```python
from geometric_lib import square
square.area(4)
// 16
```
- Функция нахождения периметра, принимает на вход одно число, сторону квадрата, а возвращает его периметр т.e. 4 стороны.
```python
from geometric_lib import square
square.perimeter(4)
// 16
```

## Triangle
- Функция нахождения площади, принимает на вход два числа, катет и высоту треугольника, а возвращает его площадь т.e. половину произведения катета на высоту.
```python
from geometric_lib import triangle
triangle.area(2, 4)
// 4
```
- Функция нахождения периметра, принимает на вход три числа, стороны треугольника, а возвращает его периметр т.e. сумму всех сторон.
```python
from geometric_lib import triangle
triangle.perimeter(1, 2, 4)
// 7
```


# История изменения проекта с хешами комитов
```hash
a184c2a6282b8a5b75b6877dc285d3aa3eafdd72 - rectange.py changed
ca6a2d88eb6d4f230232c2247dd997ae2623fc5a - triangle.py added
b2a432f4e54974384dc428bfd40b5cbd8f825533 - rectangle.py added
```
