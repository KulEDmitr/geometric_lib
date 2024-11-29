# Geometric Library

## Общее описание
Это программа для вычислений геометрических фигур, таких как круг, квадрат, прямоугольник и треугольник. Она предоставляет функции для вычисления площади и периметра каждой из фигур.

## Математические формулы

### Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = ah/2

### Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

## Описание функций

### Прямоугольник
[Сслыка](https://github.com/CalrusMagnusen/geometric_lib/blob/new_features_466905/rectangle.py)

- `area(a, b)`: Вычисляет площадь прямоугольника.
  - Пример вызова: `area(5, 3)` вернет `15`.

- `perimeter(a, b)`: Вычисляет периметр прямоугольника.
  - Пример вызова: `perimeter(5, 3)` вернет `16`.

### Треугольник
[Ссылка](https://github.com/CalrusMagnusen/geometric_lib/blob/new_features_466905/triangle.py)
- `area(a, h)`: Вычисляет площадь треугольника.
  - Пример вызова: `area(5, 4)` вернет `10.0`.

- `perimeter(a, b, c)`: Вычисляет периметр треугольника.
  - Пример вызова: `perimeter(3, 4, 5)` вернет `12`.

### Круг
[Ссылка](https://github.com/CalrusMagnusen/geometric_lib/blob/new_features_466905/circle.py)

- `area(r)`: Вычисляет площадь круга.
  - Пример вызова: `area(3)` вернет `28.27`.

- `perimeter(r)`: Вычисляет периметр круга.
  - Пример вызова: `perimeter(3)` вернет `18.85`.

### Квадрат
[Ссылка](https://github.com/CalrusMagnusen/geometric_lib/blob/new_features_466905/square.py)

- `area(a)`: Вычисляет площадь квадрата.
  - Пример вызова: `area(5)` вернет `25`.

- `perimeter(a)`: Вычисляет периметр квадрата.
  - Пример вызова: `perimeter(5)` вернет `20`.

## История изменений
- Хеш: ccafec5 
  - Коммит: Added new file rectangle.py
- Хеш: fb2ade8 
  - Коммит: bug has been fixed
- Хеш: 14b7813 
  - Коммит: readme.md has been modified
- Хеш: d600455 
  - Коммит: Added new file triangle.py

