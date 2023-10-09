# Описание проекта: 
## находит периметр и площадь геометрических фигур, таких как:
- круг
- прямоугольник
- квадрат
- треугольник
# Файлы и функции
## Методы circle.py
#### Площадь круга:
```python
def area(r):
    return math.pi * r * r

#input:  1
#output: 3.141592653589793

#input:  3
#output: 28.274333882308138
```

#### Периметр круга:
```python
def perimeter(r):
    return 2 * math.pi * r

#input:  2
#output: 12.566370614359172

#input:  5
#output: 31.41592653589793
```

## Методы rectangle.py
#### Площадь прямоугольника:
```python
def area(a, b): 
    return a * b 

#input:  2 3
#output: 6

#input:  4 5
#output: 20
```

#### Периметр прямоугольника:
```python
def perimeter(a, b): 
    return 2 * (a + b)

#input:  2 4
#output: 12

#input:  3 5
#output: 16
```

## Методы square.py
#### Площадь квадрата:
```python
def area(a):
    return a * a

#input:  4
#output: 16

#input:  8
#output: 64
```

#### Периметр квадрата:
```python
def perimeter(a):
    return 4 * a

#input:  3
#output: 12

#input:  5
#output: 20
```

## Методы triangle.py
#### Площадь треугольника:
```python
def area(a, h): 
    return a * h / 2 

#input:  2 3
#output: 3.0

#input:  5 3
#output: 7.5
```

#### Периметр треугольника:
```python
def perimeter(a, b, c): 
    return a + b + c  

#input:  3 4 5
#output: 12

#input:  5 5 6
#output: 16
```
# История коммитов
| Коммит |Дата|Ссылка на коммит|
| ----------- | ----------- | ----------- |
| 4b5332c    |20.09.2023   |https://github.com/KulEDmitr/geometric_lib/commit/4b5332c78d202dcda75c3042ef856166723a6deb|
| 8b46836    |19.09.2023   |https://github.com/KulEDmitr/geometric_lib/commit/8b46836837050ff60ad96eede52245bf0237e082|