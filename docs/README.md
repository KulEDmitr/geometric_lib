# Math formulas
## Area
- Circle: S = πR²
- Triangle: S = ah
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Triangle: P = a + b + c
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация для модулей circle.py, triangle.py и rectangle.py 

## circle.py

### Модуль для работы с кругами

```python
import math

def area(r):
    '''Вычисляет площадь круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.
    '''
    return math.pi * r * r

def perimeter(r):
    '''Вычисляет длину окружности.

    Args:
        r (float): Радиус окружности.

    Returns:
        float: Длина окружности.
    '''
    return 2 * math.pi * r
```
### Примеры использования
```python
import circle

# Вычисление площади круга с радиусом 5
area_result = circle.area(5)
print("Площадь круга:", area_result)

# Вычисление длины окружности с радиусом 7
perimeter_result = circle.perimeter(7)
print("Длина окружности:", perimeter_result)
```

## triangle.py

### Модуль для работы с треугольниками

```python
def area(a, h):
    '''Вычисляет площадь треугольника.

    Args:
        a (float): Длина основания треугольника.
        h (float): Длина высоты, опущенной к основанию.

    Returns:
        float: Площадь треугольника.
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''Вычисляет периметр треугольника.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.
    '''
    return a + b + c
```
### Примеры использования
```python
import triangle

# Пример использования:
base = 6
height = 4
area_result = triangle.area(base, height)

side1 = 3
side2 = 4
side3 = 5
perimeter_result = triangle.perimeter(side1, side2, side3)

print("Площадь треугольника:", area_result)
print("Периметр треугольника:", perimeter_result)
```
## rectangle.py

### Модуль для работы с прямоугольниками

```python
def area(a, b):
    '''Вычисляет площадь прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Площадь прямоугольника.
    '''
    return a * b

def perimeter(a, b):
    '''Вычисляет периметр прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Периметр прямоугольника.
    '''
    return (a + b) * 2
```
### Примеры использования
```python
import rectangle

# Вычисление площади прямоугольника с длинами сторон 4 и 7
area_result = rectangle.area(4, 7)
print("Площадь прямоугольника:", area_result)

# Вычисление периметра прямоугольника с длинами сторон 3 и 5
perimeter_result = rectangle.perimeter(3, 5)
print("Периметр прямоугольника:", perimeter_result)
```

## Тестирование
Для проверки работоспособности программ в папке [tests](../tests) находятся соответствующие файлы для unit тестирования

## История изменений

- `598d38e`: Изменен `rectangle.py` и добавлен `triangle.py`.
- `15ce109`: Добавлен `rectangle.py`.
- `d078c8d`: Добавлена документация.
- `8ba9aeb`: Добавлены модули `circle.py` и `square.py`.
