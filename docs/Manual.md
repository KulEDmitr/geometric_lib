# Geometric lib
## Общее описание
Geometric lib - это библтотека для языка Python, которая позволяет вычислять площадь и периметр базовых геометрических фигур.
## Функции
`circle.perimeter(r)` принимает на вход радиус круга r и возвращает периметр круга
```python
per = circle.perimeter(4) #Output: 25.132741228718345
```
`circle.area(r)` принимает на вход радиус круга r и возвращает площадь круга
```python
area = circle.area(4) #Output: 50.26548245743669
```
`rectangle.perimeter(a, b)` принимает на вход стороны прямоугольника a и b, возвращает периметр прямоугольника
```python
per = rectangle.perimeter(4, 3) #Output: 14
```
`rectangle.area(a, b)` принимает на вход стороны прямоугольника a и b, возвращает площадь прямоугольника
```python
area = rectangle.area(4, 3) #Output: 12
```
`square.perimeter(a)` принимает на вход сторону квадрата a, возвращает периметр квардата
```python
per = sqaure.perimeter(5) #Output: 25
```
`square.area(a, b)` принимает на вход сторону квадрата a, возвращает площадь квадрата
```python
area = square.area(5) #Output: 20
```
`triangle.perimeter(a, b, c)` Принимает на вход три стороны треугольника a, b и c, возвращает периметр треугольника
```python
per = triangle.perimeter(4, 5, 6) #Output: 15
```
`triangle.area(a, h)` принимает на вход сторону треугольника a и проведённую к ней высоту h, возвращает площадь треугольника
```python
area = triangle.area(4, 6) #Output: 12
```
## История изменения проекта
```
ff72acf Добавлен модуль triangle, исправлен модуль rectangle
0161d8d Добавлен модуль rectangle
d078c8d Добавлена папка docs
8ba9aeb Добавлены модули circle и square
```




