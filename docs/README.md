
# Библиотека Геометрических Вычислений

## Общее Описание

**Библиотека Геометрических Вычислений** предоставляет простой интерфейс для вычисления основных геометрических характеристик таких фигур, как круг, квадрат, прямоугольник и треугольник. Эта библиотека на Python предназначена для учебных целей, проектов и других задач, требующих базовых геометрических функций.

Основные возможности библиотеки включают:
- Вычисление площади и периметра квадрата.
- Вычисление площади и длины окружности круга.
- Вычисление площади и периметра прямоугольника.
- Вычисление площади и периметра треугольника.

## Описание Функций и Примеры Использования

### Модуль `circle.py`

#### `calculate_area(r)`

Вычисляет площадь круга с заданным радиусом `r`.

**Параметры:**
- `r` (float): Радиус круга.

**Возвращает:**
- `float`: Площадь круга.

**Пример использования:**

```python
from circle import calculate_area

result = calculate_area(5)
print(result)  # Вывод: 78.53981633974483
```

#### `calculate_circumference(r)`

Вычисляет длину окружности круга с заданным радиусом `r`.

**Параметры:**
- `r` (float): Радиус круга.

**Возвращает:**
- `float`: Длина окружности.

**Пример использования:**

```python
from circle import calculate_circumference

result = calculate_circumference(5)
print(result)  # Вывод: 31.41592653589793
```

### Модуль `square.py`

#### `square_area(side)`

Вычисляет площадь квадрата с заданной длиной стороны.

**Параметры:**
- `side` (float): Длина стороны квадрата.

**Возвращает:**
- `float`: Площадь квадрата.

**Пример использования:**

```python
from square import square_area

result = square_area(4)
print(result)  # Вывод: 16
```

#### `square_perimeter(side)`

Вычисляет периметр квадрата.

**Параметры:**
- `side` (float): Длина стороны квадрата.

**Возвращает:**
- `float`: Периметр квадрата.

**Пример использования:**

```python
from square import square_perimeter

result = square_perimeter(4)
print(result)  # Вывод: 16
```

### Модуль `rectangle.py`

#### `rectangle_area(length, width)`

Вычисляет площадь прямоугольника.

**Параметры:**
- `length` (float): Длина прямоугольника.
- `width` (float): Ширина прямоугольника.

**Возвращает:**
- `float`: Площадь прямоугольника.

**Пример использования:**

```python
from rectangle import rectangle_area

result = rectangle_area(5, 10)
print(result)  # Вывод: 50
```

#### `rectangle_perimeter(length, width)`

Вычисляет периметр прямоугольника.

**Параметры:**
- `length` (float): Длина прямоугольника.
- `width` (float): Ширина прямоугольника.

**Возвращает:**
- `float`: Периметр прямоугольника.

**Пример использования:**

```python
from rectangle import rectangle_perimeter

result = rectangle_perimeter(5, 10)
print(result)  # Вывод: 30
```

### Модуль `triangle.py`

#### `triangle_area(base, height)`

Вычисляет площадь треугольника по его основанию и высоте.

**Параметры:**
- `base` (float): Основание треугольника.
- `height` (float): Высота треугольника.

**Возвращает:**
- `float`: Площадь треугольника.

**Пример использования:**

```python
from triangle import triangle_area

result = triangle_area(6, 4)
print(result)  # Вывод: 12.0
```

#### `triangle_perimeter(a, b, c)`

Вычисляет периметр треугольника с заданными длинами сторон `a`, `b` и `c`.

**Параметры:**
- `a` (float): Длина первой стороны.
- `b` (float): Длина второй стороны.
- `c` (float): Длина третьей стороны.

**Возвращает:**
- `float`: Периметр треугольника.

**Пример использования:**

```python
from triangle import triangle_perimeter

result = triangle_perimeter(3, 4, 5)
print(result)  # Вывод: 12
```

## История Версий
- `fb082b59`**: Add new description and add README.md
- `26d75c6d`**: Circle and square added
- `4ac89ba4`**: Fix a rectangle file
- `26d75c6d`**: Add new file rectangle.py
- `8ba9aeb3`**: Circle and square added

