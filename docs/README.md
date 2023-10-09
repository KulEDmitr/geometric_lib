# Geometric Lib

Данный проект представляет собой набор модулей и функций, предназначенных для вычисления площадей и периметров различных геометрических фигур.

Проект включает следующие модули:

 *   Модуль `circle`: Позволяет вычислять площадь и периметр круга по его радиусу.
 *   Модуль `rectangle`: Содержит функции для вычисления площади и периметра прямоугольника, принимая на вход длины его сторон.
 *   Модуль `square`: Предоставляет методы для вычисления площади и периметра квадрата, исходя из длины его стороны.
 *   Модуль `triangle`: Позволяет вычислять площадь треугольника по его основанию и высоте, а также периметр по длинам его сторон.

## Модуль circle

### Функция `area(r)`

Вычисляет площадь круга по радиусу.

#### Пример использования:

```python3
import circle

radius = 5
result = circle.area(radius)
print("Площадь круга:", result)
```

### Функция `perimeter(r)`

Вычисляет периметр круга по радиусу.

#### Пример использования:

```python3
import circle

radius = 5
result = circle.perimeter(radius)
print("Периметр круга:", result)
```

## Модуль rectangle

### Функция `area(a, b)`

Вычисляет площадь прямоугольника по его сторонам.

#### Пример использования:

```python3
import rectangle

length = 4
width = 6
result = rectangle.area(length, width)
print("Площадь прямоугольника:", result)
```

### Функция `perimeter(a, b)`

Вычисляет периметр прямоугольника по его сторонам.

#### Пример использования:

```python3
import rectangle

length = 4
width = 6
result = rectangle.perimeter(length, width)
print("Периметр прямоугольника:", result)
```

## Модуль square

### Функция `area(a)`

Вычисляет площадь квадрата по его стороне.

#### Пример использования:

```python3
import square

side = 3
result = square.area(side)
print("Площадь квадрата:", result)
```

### Функция `perimeter(a)`

Вычисляет периметр квадрата по его стороне.

#### Пример использования:

```python3
import square

side = 3
result = square.perimeter(side)
print("Периметр квадрата:", result)
```

## Модуль triangle

### Функция `area(a, h)`

Вычисляет площадь треугольника по его основанию и высоте.

#### Пример использования:

```python3
import triangle

base = 8
height = 4
result = triangle.area(base, height)
print("Площадь треугольника:", result)
```

### Функция `perimeter(a, b, c)`

Вычисляет периметр треугольника по длинам его сторон.

#### Пример использования:

```python3
import triangle

side1 = 5
side2 = 6
side3 = 7
result = triangle.perimeter(side1, side2, side3)
print("Периметр треугольника:", result)
```

## История изменения проекта

```
commit 388510940b0d9b34e3a7abe42489cc9bef1736b7 (HEAD -> main, origin/main, origin/HEAD)
Author: Артур Хачатуров <wzrayyy@gmail.com>
Date:   Thu Sep 14 20:46:50 2023 +0300

    Исправлена ошибка в вычислении периметра в rectangle.py

commit bb75a6fc0c4b8d09977c2d926ef3242142992053
Author: Артур Хачатуров <wzrayyy@gmail.com>
Date:   Thu Sep 14 20:41:31 2023 +0300

    Создан файл triangle.py

commit 7b795450917f953bb51dfc3198ba13b57cb64fe7
Author: Артур Хачатуров <wzrayyy@gmail.com>
Date:   Thu Sep 14 20:38:54 2023 +0300

    Создан новый файл rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```

