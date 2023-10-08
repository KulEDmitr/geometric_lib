# Math formulas

Данный проект содержит файлы .py, в каждом из которых объявлены функции для подсчета площадей и периметров **четырех геометрических фигур**:
- Круг
- Прямоугольник
- Квадрат
- Треугольник

## Area formulas
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter formulas
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions
- ### circle.py
  - ##### area(r) 
    Принимает число r - радиус окружности, возвращает площадь круга с радиусом r (произведение числа Пи на квадрат радиуса r):
    
    ```python
    print(area(5))
    -> 78.53981633974483
    ``` 
  - ##### perimeter(r)
    Принимает число r - радиус окружности, возвращает длину окружности с радиусом r (удвоенное произведение числа Пи на радиус r):
    
    ```python
    print(perimeter(5))
    -> 31.41592653589793
    ``` 
    
- ### rectangle.py
  - ##### area(a, b)
    Принимает 2 числа: a и b, - стороны прямоугольника. Возвращает площадь прямоугольника со сторонами a и b (произведение чисел a и b):
    
    ```python
    print(area(4, 5))
    -> 20
    ``` 
  - ##### perimeter(a, b)
    Принимает 2 числа: a и b, - стороны прямоугольника. Возвращает периметр прямоугольника со сторонами a и b (удвоенную сумму чисел a и b):
    
    ```python
    print(perimeter(4, 5))
    -> 18
    ``` 

- ### square.py
  - ##### area(a)
    Принимает число a - сторону квадрата, возвращает площадь квадрата со стороной a (квадрат числа a):
    
    ```python
    print(area(5))
    -> 25
    ``` 
  - ##### perimeter(a)
    Принимает число a - сторону квадрата, возвращает периметр квадрата со стороной a (произведение числа a на 4):
    
    ```python
    print(perimeter(5))
    -> 20
    ``` 

- ### triangle.py
  - ##### area(a, h)
    Принимает 2 числа: a и h, - основание треугольника и высота к этому основанию соответственно. Возвращает площадь треугольника с основанием a и высотой к этому основанию h (половина произведения чисел a и h):
    
    ```python
    print(area(5, 4))
    -> 10
    ``` 
  - ##### perimeter(a, b, c)
    Принимает 3 числа: a, b и c, - стороны треугольника. Возвращает периметр треугольника со сторонами (половина произведения чисел a и h):
    
    ```python
    print(perimeter(3, 4, 5))
    -> 12
    ``` 
  
## Project change history
* **1fdb837** (HEAD -> main, origin/main, origin/HEAD) Updated README.md
* **f57eaaa** updated readme.md file: added description and examples of all functions from .py fies in the project, added project change history.
* **3aceafd** added comments to functions in all .py files
* **c2aa33d** (origin/main, origin/HEAD) Created triangle.py and fixed bug in calculating perimeter in rectangle.py
* **f178690** Created rectangle.py
* **d078c8d** L-03: Docs added
* **8ba9aeb** L-03: Circle and square added
