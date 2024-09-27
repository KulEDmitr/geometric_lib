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

# Описание проекта
Данный проект позволяет вычислять площади и периметры таких фигур как треугольник, круг, прямоугольник, квадрат
# Описание файлов проекта
## 1. [square.py](./square.py)
###  area
Эта функция получает длину стороны квадрата и возвращает его площадь    
Пример вызова:  
``` python
a = area(2)       
print(a)
```    
В данном случае код выведет 4   
### perimeter
Эта функция получает длину стороны квадрата и возвращает его периметер  
Пример вызова:  
``` python
a = area(2)
print(a)
```     
В данном случае код выведет 8   
## 2. [rectangle.py](./rectangle.py)
### area
Эта функция получает длины сторон прямоугольника и возвращает его площадь   
Пример вызова:  
``` python
a = area(2, 4)
print(a)
```     
В данном случае код выведет 8
### perimeter
Эта функция получает длины сторон прямоугольника и возвращает его периметер     
Пример вызова:  
``` python
a = area(2, 4)
print(a)
```     
В данном случае код выведет 12
## 3. [triangle.py](./triangle.py)
### area
Эта функция получает длину основания треугольника, длину высоты проведенной к этому основанию и возвращает его площадь  
Пример вызова:  
``` python
a = area(2, 4)
print(a)
```
В данном случае код выведет 4
### perimeter
Эта функция получает длины сторон треугольника и возвращает его периметер   
Пример вызова:  
``` python
a = perimeter(2, 4, 3)
print(a)
```     
В данном случае код выведет 9
## 4. [circle.py](./circle.py)
### area
Эта функция получает радиус круга и возвращает его площадь  
Пример вызова:  
``` python
a = area(4)
print(a)
```   
В данном случае код выведет 16pi
### perimeter
Эта функция получает радиус круга и возвращает длину его периметер  
Пример вызова:  
```` python
a = perimeter(4)
print(a)
````     
В данном случае код выведет 8pi
# История изменения проекта:
- commit fa2b4188da6b550f4fb0c284043c4d262860da2a 
  - Author: Nikolai Veselov <143344092+DirtyDevel0per@users.noreply.github.com>
  - Date:   Thu Sep 14 09:28:11 2023 +0300

      `fix mistake in rectangle.py`

- commit febfaa858a571055bcfa7c830b78de3be06d1f11
  - Author: Nikolai Veselov <143344092+DirtyDevel0per@users.noreply.github.com>
  - Date:   Thu Sep 14 09:27:17 2023 +0300

      `add new file triangle.py`

- commit 7975da63082f289daf538cfb0c1dda685ce1c3f5
  - Author: Nikolai Veselov <143344092+DirtyDevel0per@users.noreply.github.com>
  - Date:   Thu Sep 14 09:26:02 2023 +0300

    `add new file ractangle.py`

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:55:29 2021 +0300

    `L-03: Docs added`

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:54:08 2021 +0300

    `L-03: Circle and square added`
# Тесты
- [circle_test](../circle_test.py)
- [rectangle_test](../rectangle_test.py)
- [triangle_test](../triangle_test.py)
- [square_test](../square_test.py)