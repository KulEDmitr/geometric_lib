
# Geometric_lib

Данная библиотека предоставляет возможность эффективно использовать готовые формулы для вычисления параметров разных фигур.


## Используемые формулы

### Area
* Circle: S = πR²
* Rectangle: S = ab
* Square: S = a²
* Triangle: S = ah/2

### Perimeter
* Circle: P = 2πR
* Rectangle: P = 2a + 2b
* Square: P = 4a
* Triangle: P = a + b + c

## Usage/Examples

Функции возвращают периметр либо площадь фигуры

### Circle

- ### area 
Параметры: 

    r (float): радиус круга

Возвращаемое значение:

    s (float): площадь круга

Примеры вызова:

    area(1) -> 3.14159265358979323846
        
- ### perimiter 
Параметры: 

    r (float): радиус круга

Возвращаемое значение:

    p (float): периметр круга

Примеры вызова:

    area(3) -> 18.84955592153876



### Rectangle

- ### area 
Параметры: 

    a1 (float): длина стороны
    a2 (float): длины стороны

Возвращаемое значение:

    s (float): площадь прямоугольника

Примеры вызова:

    area(2, 3) -> 6
        
- ### perimiter 
Параметры: 

    a1 (float): длина стороны
    a2 (float): длины стороны

Возвращаемое значение:

    p (float): периметр прямоугольника

Примеры вызова:

    area(5, 6) -> 22


### Square

- ### area 
Параметры: 

    a (float): длина стороны

Возвращаемое значение:

    s (float): площадь квадрата

Примеры вызова:

    area(2) -> 4
        
- ### perimiter 
Параметры: 

    a (float): длина стороны

Возвращаемое значение:

    p (float): периметр квадрата

Примеры вызова:

    area(5) -> 20


### Triangle

- ### area 
Параметры: 

    a (float): длина стороны
    h (float): длина высоты, проведенной к стороне a

Возвращаемое значение:

    s (float): площадь треугольника

Примеры вызова:

    area(5, 2.5) -> 6.25
        
- ### perimiter 
Параметры: 

    a (float): длина стороны
    b (float): длина стороны
    c (float): длина стороны

Возвращаемое значение:

    p (float): периметр треугольника

Примеры вызова:

    area(3, 4, 5) -> 12

## Hashs of commits
* a49dbe8 fixed rectangle's perimeter formula
* 3dd59d9 new figure - triangle
* ec53ef4 new figure - rectangle
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added

## Tests
* rectangle
* triangle
* square
* circle

