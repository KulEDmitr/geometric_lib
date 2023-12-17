# Использованные формулы
## Круг
- Периметр: P = 2πR
- Площадь: S = πr<sup>2</sup>

## Прямоугольник
- Периметр: P = 2(a + b)
- Площадь: S = ab

## Квадрат
- Периметр: P = 4a
- Площадь: S = a<sup>2</sup>

## Треугольник
- Периметр: P = a + b + c
- Площадь: S = ah / 2

# Функции с примерами
## circle.py
### `area(r)`
Вычисляет площадь круга по радиусу.
```
>>> area(4)
50.26548245743669
>>> area(7)
153.93804002589985
```

### `perimeter(r)`
Вычисляет периметр круга (длину окружности) по радиусу.
```
>>> perimeter(3)
18.84955592153876
>>> perimeter(4.7)
29.530970943744055
```

## rectangle.py
### `area(a, b)`
Вычисляет площадь прямоугольника по смежным сторонам.
```
>>> area(4, 6)
24
>>> area(7.5, 7.5)
56.25
```

### `perimeter(a, b)`
Вычисляет периметр прямоугольника по смежным сторонам.
```
>>> perimeter(4, 5)
18
>>> perimeter(3.4, 2.25)
11.3
```

## square.py
### `area(a)`
Вычисляет площадь квадрата по стороне.
```
>>> area(3)
9
>>> area(10)
100
```

### `perimeter(a)`
Вычисляет периметр квадрата по стороне.
```
>>> perimeter(6)
24
>>> perimeter(3.14)
12.56
```

## triangle.py
### `area(a, h)`
Вычисляет площадь треугольника по стороне и высоте, проведённой к этой стороне.
```
>>> area(3, 4)
6.0
>>> area(1, 0.866)
0.433
```

### `perimeter(a, b, c)`
Вычисляет периметр треугольника по трём сторонам.
```
>>> perimeter(3, 4, 5)
12
>>> perimeter(2.236, 2.828, 3)
8.064
```

# Тесты
Тесты `python unittest` хранятся в папке `tests`.
```
circle.py: 10/12
rectangle.py: 10/14
square.py: 9/12
triangle.py: 12/15
```

# История изменения проекта
- commit `8ba9aeb3cea847b63a91ac378a2a6db758682460`
L-03: Circle and square added

- commit `d078c8d9ee6155f3cb0e577d28d337b791de28e2`
L-03: Docs added

- commit `f90d9fbf751cd622b50bf5722257b9ac89bb3364`
Added rectangle.py

- commit `a43ac941bac55065f6e4097ede6f1acc94080fdb`
Added triangle.py and fixed rectangle.py

- commit `e002627a0b7cd69b947d53f5136160edc23a1fd3`
Added documentation

- commit `ba9bf346abc70e5916271778ded38ac4444b2d84`
added tests