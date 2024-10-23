# Документация по проекту geometric_lib

## Общее описание

geometric_lib - библиотека, написанная на языке программирования Python, которая позволяет считать площадь и периметр геоометрических фигур: окружности, прямоугольника, квадрата и треугольника.
Для того, чтобы в ходе использования этой библиотеки не возникало проблем, мы строго рекомендуем подключать её к своему Python файлу следующим образом.

```python
import circle
import rectangle
import square
import trinagle
```

Так как в geometric_lib функции подсчёта площади и периметра для разных геометрических фигур имеют одинаковые анзвания (area и perimeter соответственно), то при следующем НЕПРАВИЛЬНОМ способе подключения библиотеки возникнет проблема.

```python
from circle import *
from rectangle import *
from square import *
from trinagle import *
```

Вы можете подключать только файлы с нужными для вас геометрическими фигурами.

## Примеры использования функций

### circle.py

```python
import circle
```

square(r) -> S - функция, возвращающая значение площади окружности

```python
S = circle.area(12)
print(S) # 452.3893421169302
```

perimeter(r) -> P - функция, возвращающая значение периметра окружности

```python
P = circle.perimeter(12)
print(P) # 75.39822368615503
```

### rectangle.py

```python
import rectangle
```

square(a, b) -> S - функция, возвращающая значение площади прямоугольника

```python
S = rectangle.area(1, 2)
print(S) # 2
```

perimeter(a, b) -> P - функция, возвращающая значение периметра прямоугольника

```python
P = rectangle.perimeter(1, 2)
print(P) # 6
```

### square.py

```python
import square
```

square(a) -> S - функция, возвращающая значение площади квадрата

```python
S = square.area(12)
print(S) # 144
```

perimeter(a) -> P - функция, возвращающая значение периметра квадрата

```python
P = square.perimeter(12)
print(P) # 48
```

### triangle.py

```python
import triangle
```

square(a, h) -> S - функция, возвращающая значение площади треугольника

```python
S = triangle.area(6, 8)
print(S) # 24
```

perimeter(a, b, c) -> P - функция, возвращающая значение периметра треугольника

```python
P = triangle.perimeter(6, 8, 10)
print(P) # 24
```

## История проекта

### L-03: Circle and square added (8ba9aeb3cea847b63a91ac378a2a6db758682460)

Были созданы файлы circle.py и square.py, а также добавлены соответствующие функции вычисления площадей и периметров.

### L-03: Docs added (d078c8d9ee6155f3cb0e577d28d337b791de28e2)

Была создана папка docs, в которую помещён новый файл README.md. В нём описано, какие формулу используются для подсчёта площадей и периметров разных геометрических фигур.

### New file rectangle.py added (6d9a43fd683cf767f155f647de67828fea75c359)

Был создан файл rectangle.py, а также добавлены функции подсчёта площади и периметра прямоугольника.

### Fixed error in rectangle.py (564828d5528f487e59347446156260df3526f3c9)

Была исправлена ошибка в функции подсчёта периметра прямоугольника. Добавлен новый файл triangle.py и соответствующие функции подсчёта площади и преиметра.
